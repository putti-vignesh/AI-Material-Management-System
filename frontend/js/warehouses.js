const warehouseModal = new bootstrap.Modal(document.getElementById("warehouseModal"));

async function loadWarehouses() {
  const data = await apiRequest("/warehouses");
  const tbody = document.getElementById("warehousesTableBody");
  tbody.innerHTML = data.map((item) => `
    <tr>
      <td>${item.name}</td>
      <td>${item.location || "-"}</td>
      <td>${item.capacity}</td>
      <td>${item.manager || "-"}</td>
      <td>
        <button class="btn btn-sm btn-outline-primary" onclick="editWarehouse(${item.id})">Edit</button>
        <button class="btn btn-sm btn-outline-danger" onclick="deleteWarehouse(${item.id})">Delete</button>
      </td>
    </tr>
  `).join("");
}

async function saveWarehouse() {
  const payload = {
    name: document.getElementById("name").value,
    location: document.getElementById("location").value,
    capacity: Number(document.getElementById("capacity").value),
    manager: document.getElementById("manager").value,
  };
  const id = document.getElementById("warehouseId").value;
  if (id) {
    await apiRequest(`/warehouses/${id}`, { method: "PUT", body: JSON.stringify(payload) });
  } else {
    await apiRequest("/warehouses", { method: "POST", body: JSON.stringify(payload) });
  }
  warehouseModal.hide();
  loadWarehouses();
}

async function editWarehouse(id) {
  const data = await apiRequest(`/warehouses`);
  const item = data.find((entry) => entry.id === id);
  document.getElementById("warehouseId").value = item.id;
  document.getElementById("name").value = item.name;
  document.getElementById("location").value = item.location || "";
  document.getElementById("capacity").value = item.capacity;
  document.getElementById("manager").value = item.manager || "";
  warehouseModal.show();
}

async function deleteWarehouse(id) {
  if (confirm("Delete this warehouse?")) {
    await apiRequest(`/warehouses/${id}`, { method: "DELETE" });
    loadWarehouses();
  }
}

document.getElementById("saveWarehouseBtn").addEventListener("click", saveWarehouse);
window.addEventListener("load", loadWarehouses);
