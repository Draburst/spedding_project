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
        balance = document.getElementById("balance_user");
        balance.innerHTML = `$${data['balance']}`;
        transaction = document.getElementById("transaction_history");
        transaction.innerHTML += `$${data['transactions']}`;
    });

    
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

