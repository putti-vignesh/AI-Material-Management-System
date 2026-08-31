const scrapModal = new bootstrap.Modal(document.getElementById("scrapModal"));

async function loadScraps() {
    try {
        const data = await apiRequest("/scrap-management");
        const tbody = document.getElementById("scrapTableBody");
        tbody.innerHTML = data.map((item) => `
            <tr>
                <td><strong>${item.scrap_number}</strong></td>
                <td>${item.material_name}</td>
                <td>${item.quantity}</td>
                <td><span class="badge bg-danger">${item.reason}</span></td>
                <td>${item.warehouse_name || "-"}</td>
                <td>₹${item.estimated_scrap_value || 0}</td>
                <td><span class="badge bg-secondary">${item.disposal_status}</span></td>
            </tr>
        `).join("");
    } catch (err) {
        console.error("Error loading scrap records:", err);
    }
}

async function saveScrap() {
    const payload = {
        scrap_number: document.getElementById("scrap_number").value,
        material_name: document.getElementById("material_name").value,
        quantity: Number(document.getElementById("quantity").value),
        reason: document.getElementById("reason").value,
        warehouse_name: document.getElementById("warehouse_name").value,
        estimated_scrap_value: Number(document.getElementById("estimated_scrap_value").value || 0),
        disposal_status: "Pending"
    };
    try {
        await apiRequest("/scrap-management", { method: "POST", body: JSON.stringify(payload) });
        scrapModal.hide();
        loadScraps();
    } catch (err) {
        alert("Error saving scrap record: " + err.message);
    }
}

document.getElementById("saveScrapBtn").addEventListener("click", saveScrap);
window.addEventListener("load", loadScraps);
