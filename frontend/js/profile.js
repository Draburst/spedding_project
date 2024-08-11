const $ = document.querySelector.bind(document)
const $$ = document.querySelectorAll.bind(document)

const tab = $$('.box_content .myStt .details')
const first = $('.idea .dashboard.first')
console.log(first)

const content = tab.forEach(function(item, index) {
    item.onclick = function() {
        $('.box_content .myStt .details.active').classList.remove('active')
        this.classList.add('active')

        first.style.marginLeft = -100 * index + '%'
    }
})

function getImg() {
    const input = $('.box .box_info .avatar input[type="file"]')
    const img = $('.box .box_info .avatar img')
    input.addEventListener('change', function() {
        img.src = URL.createObjectURL(input.files[0])
    })
}

getImg()

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

console.log(getCookie('token'))

fetch('http://127.0.0.1:8000/get_profile_info/', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({'token': getCookie('token')})
})
    .then(response => response.json())
    .then(data => {
        console.log(data['user_info']);
        username = document.getElementById('user_info');
        username.innerHTML = data['user_info'];

    })