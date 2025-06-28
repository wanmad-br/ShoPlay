document.getElementById('product-list').innerHTML = `
  <div class="product">
    <h2>Product Name</h2>
    <p>Description of the product.</p>
    <p>Price: $XX.XX</p>
  </div>
`;

function fetchProducts() {
  fetch('/api/products')
    .then(response => response.json())
    .then(data => {
      const productList = document.getElementById('product-list');
      productList.innerHTML = '';
      data.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.className = 'product';
        productDiv.innerHTML = `
          <h2>${product.name}</h2>
          <p>${product.description}</p>
          <p>Price: $${product.price.toFixed(2)}</p>
        `;
        productList.appendChild(productDiv);
      });
    })
    .catch(error => console.error('Error fetching products:', error));
}

document.addEventListener('DOMContentLoaded', fetchProducts);