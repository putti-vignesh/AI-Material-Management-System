const supplierModal = new bootstrap.Modal(document.getElementById("supplierModal"));

async function loadSuppliers() {
  const data = await apiRequest("/suppliers");
  const tbody = document.getElementById("suppliersTableBody");
  tbody.innerHTML = data.map((item) => `
    <tr>
      <td>${item.name}</td>
      <td>${item.contact_person || "-"}</td>
      <td>${item.email || "-"}</td>
      <td>${item.phone || "-"}</td>
      <td>
        <button class="btn btn-sm btn-outline-primary" onclick="editSupplier(${item.id})">Edit</button>
        <button class="btn btn-sm btn-outline-danger" onclick="deleteSupplier(${item.id})">Delete</button>
      </td>
    </tr>
  `).join("");
}

async function saveSupplier() {
  const payload = {
    name: document.getElementById("name").value,
    contact_person: document.getElementById("contact_person").value,
    email: document.getElementById("email").value,
    phone: document.getElementById("phone").value,
    address: document.getElementById("address").value,
  };
  const id = document.getElementById("supplierId").value;
  if (id) {
    await apiRequest(`/suppliers/${id}`, { method: "PUT", body: JSON.stringify(payload) });
  } else {
    await apiRequest("/suppliers", { method: "POST", body: JSON.stringify(payload) });
  }
  supplierModal.hide();
  loadSuppliers();
}

async function editSupplier(id) {
  const data = await apiRequest(`/suppliers`);
  const item = data.find((entry) => entry.id === id);
  document.getElementById("supplierId").value = item.id;
  document.getElementById("name").value = item.name;
  document.getElementById("contact_person").value = item.contact_person || "";
  document.getElementById("email").value = item.email || "";
  document.getElementById("phone").value = item.phone || "";
  document.getElementById("address").value = item.address || "";
  supplierModal.show();
}

async function deleteSupplier(id) {
  if (confirm("Delete this supplier?")) {
    await apiRequest(`/suppliers/${id}`, { method: "DELETE" });
    loadSuppliers();
  }
}

document.getElementById("saveSupplierBtn").addEventListener("click", saveSupplier);
window.addEventListener("load", loadSuppliers);
