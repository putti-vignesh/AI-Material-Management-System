async function loadReports() {
  try {
    const data = await apiRequest("/reports");
    document.getElementById("reportsTableBody").innerHTML = data.map((item) => `
      <tr>
        <td>${item.title}</td>
        <td>${item.report_type}</td>
        <td>${item.summary || "-"}</td>
      </tr>
    `).join("");
  } catch (error) {
    console.error(error);
  }
}

async function generateReport() {
  const payload = {
    title: "Monthly Inventory Summary",
    report_type: "Inventory",
    summary: "Inventory levels remain stable and low stock alerts were monitored.",
  };
  await apiRequest("/reports", { method: "POST", body: JSON.stringify(payload) });
  loadReports();
}

document.getElementById("generateReportBtn").addEventListener("click", generateReport);
window.addEventListener("load", loadReports);
