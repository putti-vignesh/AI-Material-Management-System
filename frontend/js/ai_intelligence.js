// AI Lead Time Predictor
document.getElementById("btnPredictLT").addEventListener("click", async () => {
    const s = document.getElementById("ltSupplier").value || "BuildCo";
    const m = document.getElementById("ltMaterial").value || "Cement";
    const box = document.getElementById("ltResult");
    box.style.display = "block";
    box.className = "alert alert-info mt-3";
    box.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Predicting lead time...';
    try {
        const res = await apiRequest(`/ai/predict-leadtime?supplier_name=${encodeURIComponent(s)}&material_name=${encodeURIComponent(m)}`);
        box.innerHTML = `<strong><i class="fas fa-clock"></i> Lead Time Prediction:</strong> Estimated delivery lead time for <strong>${res.material_name}</strong> from <strong>${res.supplier_name}</strong> is <strong>${res.predicted_lead_time_days} Days</strong> (Confidence: ${res.confidence_level}).`;
    } catch (err) {
        box.className = "alert alert-danger mt-3";
        box.textContent = "Error predicting lead time: " + err.message;
    }
});

// AI Substitute Suggestion Engine
document.getElementById("btnSuggestSub").addEventListener("click", async () => {
    const m = document.getElementById("subMaterial").value || "Cement";
    const box = document.getElementById("subResult");
    box.style.display = "block";
    box.className = "alert alert-success mt-3";
    box.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Searching substitutes...';
    try {
        const res = await apiRequest(`/ai/suggest-substitutes?material_name=${encodeURIComponent(m)}`);
        if (res.substitutes_found && res.substitutes_found.length > 0) {
            const listHtml = res.substitutes_found.map(item => `<li><strong>${item.name}</strong> (${item.available_stock} ${item.unit} available) - ${item.match_confidence}</li>`).join("");
            box.innerHTML = `<strong><i class="fas fa-check-circle"></i> In-Stock Substitutes Found for '${res.requested_material}':</strong><ul class="mb-0 mt-2">${listHtml}</ul>`;
        } else {
            box.className = "alert alert-warning mt-3";
            box.innerHTML = `<strong><i class="fas fa-info-circle"></i> Result:</strong> ${res.ai_advice}`;
        }
    } catch (err) {
        box.className = "alert alert-danger mt-3";
        box.textContent = "Error finding substitutes: " + err.message;
    }
});

// AI Wastage Anomaly & Scrap Risk Detector
document.getElementById("btnWastage").addEventListener("click", async () => {
    const box = document.getElementById("wastageResult");
    box.style.display = "block";
    box.className = "alert alert-warning";
    box.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Running risk analysis...';
    try {
        const res = await apiRequest('/ai/wastage-analysis');
        const highRisk = res.high_wastage_risk_materials.length > 0 ? res.high_wastage_risk_materials.join(", ") : "None";
        box.innerHTML = `
            <strong><i class="fas fa-shield-alt"></i> Wastage Analysis Complete:</strong><br>
            • Anomaly Status: <strong>${res.anomaly_status}</strong><br>
            • Total Scrap Logged: <strong>${res.total_scrap_quantity} units</strong> (${res.total_scrap_records} records)<br>
            • At-Risk Low Stock Items: <strong>${highRisk}</strong><br>
            • Recommendation: <em>${res.recommendation}</em>
        `;
    } catch (err) {
        box.className = "alert alert-danger";
        box.textContent = "Error performing wastage analysis: " + err.message;
    }
});

// AI Supplier Recommendation
document.getElementById("btnRecommendSupplier").addEventListener("click", async () => {
    const m = document.getElementById("recMaterial").value || "Cement";
    const box = document.getElementById("recResult");
    box.style.display = "block";
    box.className = "alert alert-info mt-3";
    box.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Ranking suppliers...';
    try {
        const res = await apiRequest(`/ai/recommend-supplier?material_name=${encodeURIComponent(m)}`);
        if (res.recommended_supplier) {
            box.innerHTML = `<strong><i class="fas fa-star text-warning"></i> AI Recommendation for '${res.material_name}':</strong><br>${res.ai_explanation}`;
        } else {
            box.textContent = res.reason || "No recommendation available.";
        }
    } catch (err) {
        box.className = "alert alert-danger mt-3";
        box.textContent = "Error recommending supplier: " + err.message;
    }
});

// AI OCR Document Scanner
document.getElementById("btnScanOcr").addEventListener("click", async () => {
    const fileInput = document.getElementById("ocrFile");
    const box = document.getElementById("ocrResult");
    box.style.display = "block";
    box.className = "alert alert-secondary mt-3";
    box.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Scanning document with AI OCR...';

    if (!fileInput.files || fileInput.files.length === 0) {
        box.className = "alert alert-warning mt-3";
        box.innerHTML = '<strong><i class="fas fa-exclamation-triangle"></i> Demo Mode:</strong> No file selected. Running sample OCR extraction...';
        setTimeout(async () => {
            const formData = new FormData();
            const blob = new Blob(["PO-2001 INV-9021 TOTAL: ₹65,000 Supplier: TechHub"], { type: "text/plain" });
            formData.append("file", blob, "invoice_sample.txt");
            try {
                const token = localStorage.getItem("token");
                const res = await fetch("http://127.0.0.1:8000/api/ai/ocr-invoice", {
                    method: "POST",
                    headers: { "Authorization": `Bearer ${token}` },
                    body: formData
                }).then(r => r.json());
                
                box.className = "alert alert-success mt-3";
                box.innerHTML = `
                    <strong><i class="fas fa-check-circle"></i> OCR Invoice Scan Complete (${res.parsed_data.confidence_score}):</strong><br>
                    • Extracted PO #: <strong>${res.parsed_data.po_number}</strong><br>
                    • Extracted Invoice #: <strong>${res.parsed_data.invoice_number}</strong><br>
                    • Extracted Vendor: <strong>${res.parsed_data.extracted_vendor}</strong><br>
                    • Extracted Total: <strong>₹${res.parsed_data.extracted_total_amount.toLocaleString()}</strong><br>
                    <em>${res.ai_summary}</em>
                `;
            } catch (err) {
                box.className = "alert alert-danger mt-3";
                box.textContent = "OCR scan failed: " + err.message;
            }
        }, 1000);
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    try {
        const token = localStorage.getItem("token");
        const res = await fetch("http://127.0.0.1:8000/api/ai/ocr-invoice", {
            method: "POST",
            headers: { "Authorization": `Bearer ${token}` },
            body: formData
        }).then(r => r.json());
        
        box.className = "alert alert-success mt-3";
        box.innerHTML = `
            <strong><i class="fas fa-check-circle"></i> OCR Invoice Scan Complete (${res.parsed_data.confidence_score}):</strong><br>
            • Extracted PO #: <strong>${res.parsed_data.po_number}</strong><br>
            • Extracted Invoice #: <strong>${res.parsed_data.invoice_number}</strong><br>
            • Extracted Vendor: <strong>${res.parsed_data.extracted_vendor}</strong><br>
            • Extracted Total: <strong>₹${res.parsed_data.extracted_total_amount.toLocaleString()}</strong><br>
            <em>${res.ai_summary}</em>
        `;
    } catch (err) {
        box.className = "alert alert-danger mt-3";
        box.textContent = "OCR scan failed: " + err.message;
    }
});
