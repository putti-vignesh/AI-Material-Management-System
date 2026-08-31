async function loadInventory() {
  const data = await apiRequest("/inventory");
  const tbody = document.getElementById("inventoryTableBody");
  tbody.innerHTML = data.map((item) => `
    <tr>
      <td>${item.material_name}</td>
      <td>${item.transaction_type}</td>
      <td>${item.quantity}</td>
      <td>${item.reference || "-"}</td>
      <td>${item.remarks || "-"}</td>
    </tr>
  `).join("");
}

async function saveInventory() {
  const payload = {
    material_name: document.getElementById("material_name").value,
    transaction_type: document.getElementById("transaction_type").value,
    quantity: Number(document.getElementById("quantity").value),
    reference: document.getElementById("reference").value,
    remarks: document.getElementById("remarks").value,
  };
  await apiRequest("/inventory", { method: "POST", body: JSON.stringify(payload) });
  bootstrap.Modal.getInstance(document.getElementById("inventoryModal")).hide();
  loadInventory();
}

document.getElementById("saveInventoryBtn").addEventListener("click", saveInventory);
window.addEventListener("load", loadInventory);
