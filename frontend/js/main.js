const sideLinks = document.querySelectorAll('.sidebar .side-menu li a:not(.logout)');

sideLinks.forEach(item => {
    const li = item.parentElement;
    item.addEventListener('click', () => {
        sideLinks.forEach(i => {
            i.parentElement.classList.remove('active');
        })
        li.classList.add('active');
    })
});

const menuBar = document.querySelector('.content nav .bx.bx-menu');
const sideBar = document.querySelector('.sidebar');

menuBar.addEventListener('click', () => {
    sideBar.classList.toggle('close');
});

const searchBtn = document.querySelector('.content nav form .form-input button');
const searchBtnIcon = document.querySelector('.content nav form .form-input button .bx');
const searchForm = document.querySelector('.content nav form');

searchBtn.addEventListener('click', function (e) {
    if (window.innerWidth < 576) {
        e.preventDefault;
        searchForm.classList.toggle('show');
        if (searchForm.classList.contains('show')) {
            searchBtnIcon.classList.replace('bx-search', 'bx-x');
        } else {
            searchBtnIcon.classList.replace('bx-x', 'bx-search');
        }
    }
});

window.addEventListener('resize', () => {
    if (window.innerWidth < 768) {
        sideBar.classList.add('close');
    } else {
        sideBar.classList.remove('close');
    }
    if (window.innerWidth > 576) {
        searchBtnIcon.classList.replace('bx-x', 'bx-search');
        searchForm.classList.remove('show');
    }
});

// Some dark part of code
// Some part of light and clear code

var token = getCookie('token');
console.log(token);

fetch("http://localhost:8000/", {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({'token': token})
})
    .then(response => response.json())
    .then(data => {
        console.log(data);
        balance = document.getElementById('balance_user');
        balance.innerHTML = `${data['balance']}$`;
        var transactions = document.getElementById('all_transactions');
        for (const transactionId in data['transactions']) {
            if (data['transactions'].hasOwnProperty(transactionId)) {
                transactions.innerHTML += `
                <div class="bottom-data">
                    <div class="orders">
                        <table>
                            <thead>
                                <tr>
                                    <th style="padding-right: 10px;">${data['transactions'][transactionId]['amount']}$</th>
                                    <th style="padding-right: 25px;">${data['transactions'][transactionId]['date']}</th>
                                    <th>${data['transactions'][transactionId]['category']}</th>
                                </tr>
                            </thead>
                        </table>
                    </div>
                    <div class="delete-button-container">
                        <button class="delete-button" onclick="deleteTransaction(${data['transactions'][transactionId]['id']})"><img src='/images/delete.png' width="40" height="40"></button>
                    </div>
                </div>`
            }
        }
    });


document.getElementById('search').addEventListener('submit', function (el) {
    el.preventDefault();
    var searchForm = document.getElementById('search');
    date = searchForm.date.value;
    console.log(date);
    fetch('http://localhost:8000/search/', {
        method: 'POST',
        body: JSON.stringify({'token': getCookie('token'), 'date': date}),
        headers: {'Content-Type': 'application/json'}
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        var transactions = document.getElementById('all_transactions');
        transactions.innerHTML = ``;
        for (const transactionId in data['transaction_list']) {
            if (data['transaction_list'].hasOwnProperty(transactionId)) {
                transactions.innerHTML += `
                <div class="bottom-data">
                    <div class="orders" id="${parseInt(data['transaction_list'][transactionId]['id'])}">
                        <table>
                            <thead>
                                <tr>
                                    <th style="padding-right: 10px;">${data['transaction_list'][transactionId]['amount']}$</th>
                                    <th style="padding-right: 25px;">${data['transaction_list'][transactionId]['date']}</th>
                                    <th>${data['transaction_list'][transactionId]['category']}</th>
                                </tr>
                            </thead>
                        </table>
                    </div>
                    <div class="delete-button-container">
                        <button class="delete-button" onclick="deleteTransaction(${data['transaction_list'][transactionId]['id']})"><img src='/images/delete.png' width="40" height="40"></button>
                    </div>  
                </div>`
            }
        }
    });
});

function deleteTransaction(id){
    fetch('http://localhost:8000/delete_transaction/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'token': getCookie('token'), 'id': id})
    })
    .then(response => response.json())
    .then(data => console.log(data));
    location.reload();
};



function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    }


function setCookie(name, value, daysToLive){
    var date = new Date();
    date.setTime(date.getTime() + daysToLive * 24 * 60 * 60 * 1000);
    var expires = `expires=${date.toUTCString}`;
    document.cookie = `${name}=${value}; ${expires}; path=/`;
}
    
function deleteCookie(name){
    setCookie(name, null, null);
}