function updateReceipt(data) {
  const receipt = document.getElementById('receipt');
  if (!receipt) return;

  const total = Number(data.total || 0).toFixed(2);
  receipt.innerHTML = `
    <h3>Order Summary</h3>
    <div class="receipt-item">
      <p><strong>${data.item.name}</strong></p>
      <p>Qty: ${data.quantity}</p>
      <p>Unit Price: ${Number(data.item.price).toFixed(2)} gold</p>
      <p>Total: ${total} gold</p>
    </div>
  `;
}

async function handlePurchase(event) {
  const button = event.currentTarget;
  const itemId = Number(button.dataset.itemId);

  const response = await fetch('/api/purchase', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ item_id: itemId, quantity: 1 })
  });

  const data = await response.json();
  if (response.ok && data.status === 'success') {
    updateReceipt(data);
    return;
  }

  const receipt = document.getElementById('receipt');
  receipt.innerHTML = `
    <h3>Order Summary</h3>
    <p class="empty-state">${data.message || 'Unable to complete the purchase.'}</p>
  `;
}

function attachPurchaseHandlers() {
  const buttons = document.querySelectorAll('.buy-btn');
  buttons.forEach((button) => {
    button.addEventListener('click', handlePurchase);
  });
}

document.addEventListener('DOMContentLoaded', attachPurchaseHandlers);