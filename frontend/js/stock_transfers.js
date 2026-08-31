const transferModal = new bootstrap.Modal(document.getElementById("transferModal"));

async function loadTransfers() {
    try {
        const data = await apiRequest("/stock-transfers");
        const tbody = document.getElementById("transferTableBody");
        tbody.innerHTML = data.map((item) => `
            <tr>
                <td><strong>${item.transfer_number}</strong></td>
                <td>${item.material_name}</td>
                <td>${item.source_warehouse}</td>
                <td>${item.destination_warehouse}</td>
                <td>${item.quantity}</td>
                <td><span class="badge bg-success">${item.status}</span></td>
                <td>${new Date(item.transfer_date).toLocaleDateString()}</td>
            </tr>
        `).join("");
    } catch (err) {
        console.error("Error loading stock transfers:", err);
    }
}

async function saveTransfer() {
    const payload = {
        transfer_number: document.getElementById("transfer_number").value,
        material_name: document.getElementById("material_name").value,
        source_warehouse: document.getElementById("source_warehouse").value,
        destination_warehouse: document.getElementById("destination_warehouse").value,
        quantity: Number(document.getElementById("quantity").value),
        remarks: document.getElementById("remarks").value,
        status: "Completed"
    };
    try {
        await apiRequest("/stock-transfers", { method: "POST", body: JSON.stringify(payload) });
        transferModal.hide();
        loadTransfers();
    } catch (err) {
        alert("Error executing transfer: " + err.message);
    }
}

document.getElementById("saveTransferBtn").addEventListener("click", saveTransfer);
window.addEventListener("load", loadTransfers);
