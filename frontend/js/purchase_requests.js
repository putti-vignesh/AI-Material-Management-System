const requestModal = new bootstrap.Modal(document.getElementById("requestModal"));

async function loadRequests() {
  const data = await apiRequest("/purchase-requests");
  const tbody = document.getElementById("requestsTableBody");
  tbody.innerHTML = data.map((item) => `
    <tr>
      <td>${item.request_number}</td>
      <td>${item.material_name}</td>
      <td>${item.quantity}</td>
      <td>${item.status}</td>
      <td>
        <button class="btn btn-sm btn-outline-primary" onclick="editRequest(${item.id})">Edit</button>
        <button class="btn btn-sm btn-outline-success" onclick="approveRequest(${item.id})">Approve</button>
      </td>
    </tr>
  `).join("");
}

async function saveRequest() {
  const payload = {
    request_number: document.getElementById("request_number").value,
    material_name: document.getElementById("material_name").value,
    quantity: Number(document.getElementById("quantity").value),
    supplier: document.getElementById("supplier").value,
    priority: document.getElementById("priority").value,
    status: document.getElementById("status").value,
    remarks: document.getElementById("remarks").value,
  };
  const id = document.getElementById("requestId").value;
  if (id) {
    await apiRequest(`/purchase-requests/${id}`, { method: "PUT", body: JSON.stringify(payload) });
  } else {
    await apiRequest("/purchase-requests", { method: "POST", body: JSON.stringify(payload) });
  }
  requestModal.hide();
  loadRequests();
}

async function editRequest(id) {
  const data = await apiRequest(`/purchase-requests`);
  const item = data.find((entry) => entry.id === id);
  document.getElementById("requestId").value = item.id;
  document.getElementById("request_number").value = item.request_number;
  document.getElementById("material_name").value = item.material_name;
  document.getElementById("quantity").value = item.quantity;
  document.getElementById("supplier").value = item.supplier || "";
  document.getElementById("priority").value = item.priority;
  document.getElementById("status").value = item.status;
  document.getElementById("remarks").value = item.remarks || "";
  requestModal.show();
}

async function approveRequest(id) {
  const data = await apiRequest(`/purchase-requests`);
  const item = data.find((entry) => entry.id === id);
  item.status = "Approved";
  await apiRequest(`/purchase-requests/${id}`, { method: "PUT", body: JSON.stringify(item) });
  loadRequests();
}

document.getElementById("saveRequestBtn").addEventListener("click", saveRequest);
window.addEventListener("load", loadRequests);
