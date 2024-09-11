const API_URL = 'http://localhost:8000/api/products/';

document.getElementById('product-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const description = document.getElementById('description').value;
    const price = parseFloat(document.getElementById('price').value);

    const xhr = new XMLHttpRequest();
    xhr.open('POST', API_URL, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
        if (xhr.status >= 200 && xhr.status < 300) {
            document.getElementById('product-form').reset();

            loadProducts();
        } else {
            console.error('Error:', xhr.statusText);
            alert('Error adding product');
        }
    };
    xhr.onerror = function() {
        console.error('Request failed');
        alert('Error adding product');
    };
    xhr.send(JSON.stringify({ name, description, price }));
});

function loadProducts() {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', API_URL, true);
    xhr.onload = function() {
        if (xhr.status >= 200 && xhr.status < 300) {
            const products = JSON.parse(xhr.responseText);
            const tableBody = document.querySelector('#product-table tbody');
            tableBody.innerHTML = '';

            products.forEach(product => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${product.name}</td>
                    <td>${product.description}</td>
                    <td>${product.price}</td>
                `;
                tableBody.appendChild(row);
            });
        } else {
            console.error('Error:', xhr.statusText);
            alert('Error loading products');
        }
    };
    xhr.onerror = function() {
        console.error('Request failed');
        alert('Error loading products');
    };
    xhr.send();
}

loadProducts();