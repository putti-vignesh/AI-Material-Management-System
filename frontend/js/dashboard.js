async function loadDashboard() {
  try {
    const summary = await apiRequest("/dashboard");
    document.getElementById("materialCount").textContent = summary.material_count;
    document.getElementById("supplierCount").textContent = summary.supplier_count;
    document.getElementById("warehouseCount").textContent = summary.warehouse_count;
    document.getElementById("requestCount").textContent = summary.pending_requests;

    const list = document.getElementById("recentTransactions");
    list.innerHTML = summary.low_stock.length
      ? summary.low_stock.map((item) => `<li class="list-group-item">${item} is below minimum stock</li>`).join("")
      : '<li class="list-group-item">No low stock alerts</li>';

    const ctx = document.getElementById("stockChart");
    if (ctx) {
      new Chart(ctx, {
        type: "bar",
        data: {
          labels: ["Materials", "Suppliers", "Warehouses", "Pending Requests"],
          datasets: [{ label: "Overview", data: [summary.material_count, summary.supplier_count, summary.warehouse_count, summary.pending_requests], backgroundColor: ["#2563eb", "#14b8a6", "#f59e0b", "#ef4444"] }],
        },
      });
    }
  } catch (error) {
    console.error(error);
  }
}

async function askChatbot() {
  const input = document.getElementById("chatInput");
  const output = document.getElementById("chatOutput");
  if (!input || !output) return;
  output.textContent = "Thinking...";
  try {
    const response = await fetch(`${API_BASE}/chatbot?query=${encodeURIComponent(input.value)}`, {
      method: "POST",
      headers: setAuthHeader({ "Content-Type": "application/json" }),
    });
    const data = await response.json();
    output.textContent = data.answer || "No response";
  } catch (error) {
    output.textContent = error.message;
  }
}

document.getElementById("chatButton")?.addEventListener("click", askChatbot);
window.addEventListener("load", loadDashboard);
