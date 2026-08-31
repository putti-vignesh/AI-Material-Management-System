let currentInspectionId = null;
const inspectionModal = new bootstrap.Modal(document.getElementById('addInspectionModal'));

async function loadInspections() {
    try {
        const inspections = await apiRequest('/quality_inspections');
        
        const tableBody = document.querySelector('#inspectionsTable tbody');
        tableBody.innerHTML = '';
        
        if (!inspections || inspections.length === 0) {
            document.getElementById('noData').style.display = 'block';
            document.getElementById('inspectionsTable').style.display = 'none';
        } else {
            document.getElementById('noData').style.display = 'none';
            document.getElementById('inspectionsTable').style.display = 'table';
            
            inspections.forEach(inspection => {
                const row = document.createElement('tr');
                const statusColor = getStatusColor(inspection.quality_status);
                row.innerHTML = `
                    <td><strong>${inspection.grn_number}</strong></td>
                    <td>${inspection.material_name}</td>
                    <td>${inspection.batch_number || '-'}</td>
                    <td>${inspection.ordered_quantity}</td>
                    <td>${inspection.received_quantity}</td>
                    <td><span class="badge bg-success">${inspection.accepted_quantity}</span></td>
                    <td><span class="badge bg-danger">${inspection.rejected_quantity}</span></td>
                    <td><span class="badge ${statusColor}">${inspection.quality_status}</span></td>
                    <td>${inspection.inspector_name || '-'}</td>
                    <td>
                        <button class="btn btn-sm btn-info" onclick="editInspection(${inspection.id})">
                            <i class="fas fa-edit"></i>
                        </button>
                        <button class="btn btn-sm btn-danger" onclick="deleteInspection(${inspection.id})">
                            <i class="fas fa-trash"></i>
                        </button>
                    </td>
                `;
                tableBody.appendChild(row);
            });
        }
        
        updateStats(inspections || []);
    } catch (error) {
        console.error('Error loading inspections:', error);
    }
}

function updateStats(inspections) {
    const total = inspections.length;
    const approved = inspections.filter(i => i.quality_status === 'Approved').length;
    const pending = inspections.filter(i => i.quality_status === 'Pending').length;
    const rejected = inspections.filter(i => i.quality_status === 'Rejected').length;
    
    document.getElementById('totalInspections').textContent = total;
    document.getElementById('approvedCount').textContent = approved;
    document.getElementById('pendingCount').textContent = pending;
    document.getElementById('rejectedCount').textContent = rejected;
}

function getStatusColor(status) {
    const colors = {
        'Pending': 'bg-warning',
        'Approved': 'bg-success',
        'Rejected': 'bg-danger',
        'Partial': 'bg-info'
    };
    return colors[status] || 'bg-secondary';
}

async function editInspection(id) {
    try {
        const inspection = await apiRequest(`/quality_inspections/${id}`);
        
        document.getElementById('grnNumber').value = inspection.grn_number;
        document.getElementById('purchaseRequestId').value = inspection.purchase_request_id;
        document.getElementById('materialName').value = inspection.material_name;
        document.getElementById('batchNumber').value = inspection.batch_number || '';
        document.getElementById('orderedQuantity').value = inspection.ordered_quantity;
        document.getElementById('receivedQuantity').value = inspection.received_quantity;
        document.getElementById('acceptedQuantity').value = inspection.accepted_quantity;
        document.getElementById('rejectedQuantity').value = inspection.rejected_quantity;
        document.getElementById('inspectorName').value = inspection.inspector_name || '';
        document.getElementById('qualityStatus').value = inspection.quality_status;
        document.getElementById('warehouseLocation').value = inspection.warehouse_location || '';
        document.getElementById('inspectionRemarks').value = inspection.inspection_remarks || '';
        document.getElementById('defectsFound').value = inspection.defects_found || '';
        
        document.getElementById('modalTitle').textContent = 'Edit Quality Inspection';
        currentInspectionId = id;
        inspectionModal.show();
    } catch (error) {
        console.error('Error loading inspection:', error);
        alert('Failed to load inspection details');
    }
}

async function deleteInspection(id) {
    if (!confirm('Are you sure you want to delete this inspection?')) return;
    
    try {
        await apiRequest(`/quality_inspections/${id}`, {
            method: 'DELETE'
        });
        alert('Inspection deleted successfully');
        loadInspections();
    } catch (error) {
        console.error('Error deleting inspection:', error);
        alert('Error deleting inspection: ' + error.message);
    }
}

document.getElementById('saveInspectionBtn').addEventListener('click', async () => {
    const grnNumber = document.getElementById('grnNumber').value;
    const purchaseRequestId = document.getElementById('purchaseRequestId').value;
    const materialName = document.getElementById('materialName').value;
    const batchNumber = document.getElementById('batchNumber').value;
    const orderedQuantity = parseFloat(document.getElementById('orderedQuantity').value);
    const receivedQuantity = parseFloat(document.getElementById('receivedQuantity').value);
    const acceptedQuantity = parseFloat(document.getElementById('acceptedQuantity').value);
    const rejectedQuantity = parseFloat(document.getElementById('rejectedQuantity').value);
    const inspectorName = document.getElementById('inspectorName').value;
    const qualityStatus = document.getElementById('qualityStatus').value;
    const warehouseLocation = document.getElementById('warehouseLocation').value;
    const inspectionRemarks = document.getElementById('inspectionRemarks').value;
    const defectsFound = document.getElementById('defectsFound').value;
    
    if (!grnNumber || !purchaseRequestId || !materialName || isNaN(orderedQuantity) || isNaN(receivedQuantity) || isNaN(acceptedQuantity) || isNaN(rejectedQuantity)) {
        alert('Please fill in all required fields');
        return;
    }
    
    const payload = {
        grn_number: grnNumber,
        purchase_request_id: purchaseRequestId,
        material_name: materialName,
        batch_number: batchNumber,
        ordered_quantity: orderedQuantity,
        received_quantity: receivedQuantity,
        accepted_quantity: acceptedQuantity,
        rejected_quantity: rejectedQuantity,
        inspector_name: inspectorName,
        quality_status: qualityStatus,
        warehouse_location: warehouseLocation,
        inspection_remarks: inspectionRemarks,
        defects_found: defectsFound
    };
    
    try {
        if (currentInspectionId) {
            await apiRequest(`/quality_inspections/${currentInspectionId}`, {
                method: 'PUT',
                body: JSON.stringify(payload)
            });
            alert('Inspection updated successfully');
        } else {
            await apiRequest('/quality_inspections', {
                method: 'POST',
                body: JSON.stringify(payload)
            });
            alert('Inspection created successfully');
        }
        
        inspectionModal.hide();
        resetForm();
        currentInspectionId = null;
        loadInspections();
    } catch (error) {
        console.error('Error saving inspection:', error);
        alert('Error: ' + error.message);
    }
});

function resetForm() {
    document.getElementById('inspectionForm').reset();
    document.getElementById('modalTitle').textContent = 'Add Quality Inspection';
    currentInspectionId = null;
}

document.getElementById('addInspectionModal').addEventListener('hidden.bs.modal', resetForm);

// Load inspections on page load
document.addEventListener('DOMContentLoaded', loadInspections);
