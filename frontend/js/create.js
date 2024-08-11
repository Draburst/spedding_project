
fetch('http://localhost:8000/create_transaction/')
    .then(response => response.json())
    .then(data => {
        console.log(data)
        var transactions = document.getElementById('category');
        transactions.innerHTML = ``
        for (const transactionId in data['category_list']) {
            console.log(transactionId);
            if (data['category_list'].hasOwnProperty(transactionId)) {
                transactions.innerHTML += `<option value="${data['category_list'][transactionId]['id']}">${data['category_list'][transactionId]['name']}</option>`;
            }
        };
        }
    );


document.getElementById('transaction_form').addEventListener('submit', function(el){
    el.preventDefault();
    var transactionForm = document.getElementById('transaction_form');
    var amount = transactionForm.amount.value;
    var date = transactionForm.date.value;
    var categoryId = transactionForm.category.value;
    var token = getCookie('token');
    console.log(token)

    fetch('http://localhost:8000/create_transaction/', {
        method: 'POST',
        headers: {'Content-type': 'application/json'},
        body: JSON.stringify({'token': token, 'amount': amount, 'date': date, 'category': categoryId})
    })
    .then(response => response.json())
    .then(data => window.location.href='main.html');
});
    


function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    }