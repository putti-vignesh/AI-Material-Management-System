let currentGRNId = null;
const grnModal = new bootstrap.Modal(document.getElementById('addGRNModal'));

async function loadGRNs() {
    try {
        const grns = await apiRequest('/goods_receiving');
        
        const tableBody = document.querySelector('#grnsTable tbody');
        tableBody.innerHTML = '';
        
        if (!grns || grns.length === 0) {
            document.getElementById('noData').style.display = 'block';
            document.getElementById('grnsTable').style.display = 'none';
        } else {
            document.getElementById('noData').style.display = 'none';
            document.getElementById('grnsTable').style.display = 'table';
            
            grns.forEach(grn => {
                const row = document.createElement('tr');
                const statusColor = getStatusColor(grn.receiving_status);
                const receivingDate = new Date(grn.receiving_date).toLocaleDateString();
                row.innerHTML = `
                    <td><strong>${grn.grn_number}</strong></td>
                    <td>${grn.po_number}</td>
                    <td>${grn.supplier_name}</td>
                    <td>${grn.material_name}</td>
                    <td>${grn.ordered_quantity}</td>
                    <td>${grn.received_quantity}</td>
                    <td>${grn.unit}</td>
                    <td><span class="badge ${statusColor}">${grn.receiving_status}</span></td>
                    <td>${receivingDate}</td>
                    <td>
                        <button class="btn btn-sm btn-info" onclick="editGRN(${grn.id})">
                            <i class="fas fa-edit"></i>
                        </button>
                        <button class="btn btn-sm btn-danger" onclick="deleteGRN(${grn.id})">
                            <i class="fas fa-trash"></i>
                        </button>
                    </td>
                `;
                tableBody.appendChild(row);
            });
        }
        
        updateStats(grns || []);
    } catch (error) {
        console.error('Error loading GRNs:', error);
    }
}

function updateStats(grns) {
    const total = grns.length;
    const approved = grns.filter(g => g.receiving_status === 'QC Approved').length;
    const pendingQC = grns.filter(g => g.receiving_status === 'Pending QC').length;
    const rejected = grns.filter(g => g.receiving_status === 'Rejected').length;
    
    document.getElementById('totalGRNs').textContent = total;
    document.getElementById('approvedCount').textContent = approved;
    document.getElementById('pendingQCCount').textContent = pendingQC;
    document.getElementById('rejectedCount').textContent = rejected;
}

function getStatusColor(status) {
    const colors = {
        'Received': 'bg-info',
        'Pending QC': 'bg-warning',
        'QC Approved': 'bg-success',
        'Rejected': 'bg-danger'
    };
    return colors[status] || 'bg-secondary';
}

async function editGRN(id) {
    try {
        const grn = await apiRequest(`/goods_receiving/${id}`);
        
        document.getElementById('grnNumber').value = grn.grn_number;
        document.getElementById('poNumber').value = grn.po_number;
        document.getElementById('supplierName').value = grn.supplier_name;
        document.getElementById('materialName').value = grn.material_name;
        document.getElementById('batchNumber').value = grn.batch_number || '';
        document.getElementById('unit').value = grn.unit;
        document.getElementById('orderedQuantity').value = grn.ordered_quantity;
        document.getElementById('receivedQuantity').value = grn.received_quantity;
        document.getElementById('receivedBy').value = grn.received_by || '';
        document.getElementById('warehouseLocation').value = grn.warehouse_location || '';
        document.getElementById('invoiceNumber').value = grn.invoice_number || '';
        document.getElementById('receivingStatus').value = grn.receiving_status;
        document.getElementById('transportDetails').value = grn.transport_details || '';
        document.getElementById('damageOrShort').value = grn.damage_or_short || '';
        document.getElementById('remarks').value = grn.remarks || '';
        
        document.getElementById('modalTitle').textContent = 'Edit Goods Receiving Note';
        currentGRNId = id;
        grnModal.show();
    } catch (error) {
        console.error('Error loading GRN:', error);
        alert('Failed to load GRN details');
    }
}

async function deleteGRN(id) {
    if (!confirm('Are you sure you want to delete this GRN?')) return;
    
    try {
        await apiRequest(`/goods_receiving/${id}`, {
            method: 'DELETE'
        });
        alert('GRN deleted successfully');
        loadGRNs();
    } catch (error) {
        console.error('Error deleting GRN:', error);
        alert('Error deleting GRN: ' + error.message);
    }
}

document.getElementById('saveGRNBtn').addEventListener('click', async () => {
    const grnNumber = document.getElementById('grnNumber').value;
    const poNumber = document.getElementById('poNumber').value;
    const supplierName = document.getElementById('supplierName').value;
    const materialName = document.getElementById('materialName').value;
    const batchNumber = document.getElementById('batchNumber').value;
    const unit = document.getElementById('unit').value;
    const orderedQuantity = parseFloat(document.getElementById('orderedQuantity').value);
    const receivedQuantity = parseFloat(document.getElementById('receivedQuantity').value);
    const receivedBy = document.getElementById('receivedBy').value;
    const warehouseLocation = document.getElementById('warehouseLocation').value;
    const invoiceNumber = document.getElementById('invoiceNumber').value;
    const receivingStatus = document.getElementById('receivingStatus').value;
    const transportDetails = document.getElementById('transportDetails').value;
    const damageOrShort = document.getElementById('damageOrShort').value;
    const remarks = document.getElementById('remarks').value;
    
    if (!grnNumber || !poNumber || !supplierName || !materialName || !unit || isNaN(orderedQuantity) || isNaN(receivedQuantity)) {
        alert('Please fill in all required fields');
        return;
    }
    
    const payload = {
        grn_number: grnNumber,
        po_number: poNumber,
        supplier_name: supplierName,
        material_name: materialName,
        batch_number: batchNumber,
        unit: unit,
        ordered_quantity: orderedQuantity,
        received_quantity: receivedQuantity,
        received_by: receivedBy,
        warehouse_location: warehouseLocation,
        invoice_number: invoiceNumber,
        receiving_status: receivingStatus,
        transport_details: transportDetails,
        damage_or_short: damageOrShort,
        remarks: remarks
    };
    
    try {
        if (currentGRNId) {
            await apiRequest(`/goods_receiving/${currentGRNId}`, {
                method: 'PUT',
                body: JSON.stringify(payload)
            });
            alert('GRN updated successfully');
        } else {
            await apiRequest('/goods_receiving', {
                method: 'POST',
                body: JSON.stringify(payload)
            });
            alert('GRN created successfully');
        }
        
        grnModal.hide();
        resetForm();
        currentGRNId = null;
        loadGRNs();
    } catch (error) {
        console.error('Error saving GRN:', error);
        alert('Error: ' + error.message);
    }
});

function resetForm() {
    document.getElementById('grnForm').reset();
    document.getElementById('modalTitle').textContent = 'Create Goods Receiving Note';
    currentGRNId = null;
}

document.getElementById('addGRNModal').addEventListener('hidden.bs.modal', resetForm);

// Load GRNs on page load
document.addEventListener('DOMContentLoaded', loadGRNs);
