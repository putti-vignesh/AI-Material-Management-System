const materialModal = new bootstrap.Modal(document.getElementById("materialModal"));

async function loadMaterials() {
  const data = await apiRequest("/materials");
  const tbody = document.getElementById("materialsTableBody");
  tbody.innerHTML = data.map((item) => {
    const reserved = item.reserved_quantity || 0;
    const price = item.unit_price || 0;
    const totalValuation = item.quantity * price;
    return `
    <tr>
      <td><strong>${item.material_id}</strong></td>
      <td>${item.name}</td>
      <td>${item.category}</td>
      <td>${item.quantity} ${item.unit}</td>
      <td><span class="badge bg-warning text-dark">${reserved} ${item.unit}</span></td>
      <td>₹${price}</td>
      <td><strong>₹${totalValuation.toLocaleString()}</strong></td>
      <td><span class="badge ${item.status === 'Active' ? 'bg-success' : 'bg-secondary'}">${item.status}</span></td>
      <td>
        <button class="btn btn-sm btn-outline-primary" onclick="editMaterial(${item.id})">Edit</button>
        <button class="btn btn-sm btn-outline-danger" onclick="deleteMaterial(${item.id})">Delete</button>
      </td>
    </tr>
  `;
  }).join("");
}

async function saveMaterial() {
  const payload = {
    material_id: document.getElementById("material_id").value,
    name: document.getElementById("name").value,
    category: document.getElementById("category").value,
    unit: document.getElementById("unit").value,
    quantity: Number(document.getElementById("quantity").value),
    reserved_quantity: Number(document.getElementById("reserved_quantity").value || 0),
    unit_price: Number(document.getElementById("unit_price").value || 0),
    minimum_stock: Number(document.getElementById("minimum_stock").value),
    reorder_level: Number(document.getElementById("reorder_level").value),
    storage_location: document.getElementById("storage_location").value,
    supplier: document.getElementById("supplier").value,
    specifications: document.getElementById("specifications").value,
    storage_rules: document.getElementById("storage_rules").value,
    status: document.getElementById("status").value,
  };
  const id = document.getElementById("materialId").value;
  try {
    if (id) {
      await apiRequest(`/materials/${id}`, { method: "PUT", body: JSON.stringify(payload) });
    } else {
      await apiRequest("/materials", { method: "POST", body: JSON.stringify(payload) });
    }
    materialModal.hide();
    loadMaterials();
  } catch (err) {
    alert("Error saving material: " + err.message);
  }
}

async function editMaterial(id) {
  const data = await apiRequest(`/materials`);
  const item = data.find((entry) => entry.id === id);
  document.getElementById("materialId").value = item.id;
  document.getElementById("material_id").value = item.material_id;
  document.getElementById("name").value = item.name;
  document.getElementById("category").value = item.category;
  document.getElementById("unit").value = item.unit;
  document.getElementById("quantity").value = item.quantity;
  document.getElementById("reserved_quantity").value = item.reserved_quantity || 0;
  document.getElementById("unit_price").value = item.unit_price || 0;
  document.getElementById("minimum_stock").value = item.minimum_stock;
  document.getElementById("reorder_level").value = item.reorder_level;
  document.getElementById("storage_location").value = item.storage_location || "";
  document.getElementById("supplier").value = item.supplier || "";
  document.getElementById("specifications").value = item.specifications || "";
  document.getElementById("storage_rules").value = item.storage_rules || "";
  document.getElementById("status").value = item.status;
  materialModal.show();
}

async function deleteMaterial(id) {
  if (confirm("Delete this material?")) {
    await apiRequest(`/materials/${id}`, { method: "DELETE" });
    loadMaterials();
  }
}

document.getElementById("saveMaterialBtn").addEventListener("click", saveMaterial);
window.addEventListener("load", loadMaterials);
