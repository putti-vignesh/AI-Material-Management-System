const returnModal = new bootstrap.Modal(document.getElementById("returnModal"));

async function loadReturns() {
    try {
        const data = await apiRequest("/material-returns");
        const tbody = document.getElementById("returnsTableBody");
        tbody.innerHTML = data.map((item) => `
            <tr>
                <td><strong>${item.return_number}</strong></td>
                <td>${item.material_name}</td>
                <td>${item.supplier_name}</td>
                <td>${item.quantity}</td>
                <td><span class="badge bg-warning text-dark">${item.reason}</span></td>
                <td><span class="badge bg-info">${item.status}</span></td>
                <td>${new Date(item.return_date).toLocaleDateString()}</td>
            </tr>
        `).join("");
    } catch (err) {
        console.error("Error loading material returns:", err);
    }
}

async function saveReturn() {
    const payload = {
        return_number: document.getElementById("return_number").value,
        material_name: document.getElementById("material_name").value,
        supplier_name: document.getElementById("supplier_name").value,
        quantity: Number(document.getElementById("quantity").value),
        reason: document.getElementById("reason").value,
        status: "Returned"
    };
    try {
        await apiRequest("/material-returns", { method: "POST", body: JSON.stringify(payload) });
        returnModal.hide();
        loadReturns();
    } catch (err) {
        alert("Error saving return record: " + err.message);
    }
}

document.getElementById("saveReturnBtn").addEventListener("click", saveReturn);
window.addEventListener("load", loadReturns);
