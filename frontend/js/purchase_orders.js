const poModal = new bootstrap.Modal(document.getElementById("poModal"));

async function loadPOs() {
    try {
        const data = await apiRequest("/purchase-orders");
        const tbody = document.getElementById("poTableBody");
        tbody.innerHTML = data.map((item) => `
            <tr>
                <td><strong>${item.po_number}</strong></td>
                <td>${item.request_number || "-"}</td>
                <td>${item.supplier_name}</td>
                <td>${item.material_name}</td>
                <td>${item.quantity}</td>
                <td>₹${item.unit_price}</td>
                <td>₹${item.quantity * item.unit_price}</td>
                <td><span class="badge bg-info">${item.status}</span></td>
                <td>
                    <button class="btn btn-sm btn-outline-danger" onclick="deletePO(${item.id})">Delete</button>
                </td>
            </tr>
        `).join("");
    } catch (err) {
        console.error("Error loading POs:", err);
    }
}

async function savePO() {
    const qty = Number(document.getElementById("quantity").value);
    const unitPrice = Number(document.getElementById("unit_price").value);
    const payload = {
        po_number: document.getElementById("po_number").value,
        request_number: document.getElementById("request_number").value,
        supplier_name: document.getElementById("supplier_name").value,
        material_name: document.getElementById("material_name").value,
        quantity: qty,
        unit_price: unitPrice,
        total_amount: qty * unitPrice,
        status: document.getElementById("status").value,
    };
    try {
        await apiRequest("/purchase-orders", { method: "POST", body: JSON.stringify(payload) });
        poModal.hide();
        loadPOs();
    } catch (err) {
        alert("Error saving Purchase Order: " + err.message);
    }
}

async function deletePO(id) {
    if (confirm("Delete this purchase order?")) {
        await apiRequest(`/purchase-orders/${id}`, { method: "DELETE" });
        loadPOs();
    }
}

document.getElementById("aiRecommendBtn").addEventListener("click", async () => {
    const mat = document.getElementById("aiMaterialQuery").value;
    const resBox = document.getElementById("aiRecommendResult");
    if (!mat) {
        alert("Please enter a material name first");
        return;
    }
    resBox.style.display = "block";
    resBox.textContent = "Analyzing supplier performance with AI...";
    try {
        const data = await apiRequest(`/ai/recommend-supplier?material_name=${encodeURIComponent(mat)}`);
        if (data.recommended_supplier) {
            resBox.className = "alert alert-success mt-2";
            resBox.innerHTML = `<strong><i class="fas fa-check-circle"></i> AI Recommendation:</strong> ${data.ai_explanation} (Est. Lead Time: ${data.recommended_supplier.estimated_lead_time_days} days)`;
        } else {
            resBox.className = "alert alert-warning mt-2";
            resBox.textContent = data.reason || "No recommendation available.";
        }
    } catch (err) {
        resBox.className = "alert alert-danger mt-2";
        resBox.textContent = "AI Recommendation Error: " + err.message;
    }
});

document.getElementById("savePOBtn").addEventListener("click", savePO);
window.addEventListener("load", loadPOs);
