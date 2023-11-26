const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});

document.getElementById("form_signup").addEventListener('submit', function(el){
    el.preventDefault();
    var signupForm = document.getElementById("form_signup");
    var username = signupForm.username1.value;
    var password1 = signupForm.password1.value;
    var password2 = signupForm.password2.value;
    var email = signupForm.email1.value;

    fetch('http://127.0.0.1:8000/auth/signup', {
        method:'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({"username": username, "password1": password1,"password2": password2, "email": email})
    })

    .then(response => response.json())
    .then(data => {
        if(data['token']){
            setCookie('token', data['token'], 10);
            window.location.href='main.html';
        }
        else {
            let error_line = document.getElementById('signup_error_line')
            error_line.innerHTML = `${JSON.stringify(data['errors'])}`
        }
    })
}) 

document.getElementById("form_signin").addEventListener('submit', function(el){
    el.preventDefault();
    var signupForm = document.getElementById("form_signin");
    var username = signupForm.username.value;
    var password = signupForm.password.value;

    fetch('http://127.0.0.1:8000/auth/login', {
        method:'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({"username": username, "password": password})
    })

    .then(response => response.json())
    .then(data => {
        if (data['token']) {
            deleteCookie('token');
            setCookie('token', data['token'], 10);
            window.location.href='main.html';
        }

        else {
            let error_line = document.getElementById('signin_error_line')
            error_line.innerHTML = `${data['errors']}`
        }
    })
}) 

// Logic of set Cookies: 'name=value; expires=100; path=/'
function setCookie(name, value, daysToLive){
    var date = new Date();
    date.setTime(date.getTime() + daysToLive * 24 * 60 * 60 * 1000);
    var expires = `expires=${date.toUTCString}`;
    document.cookie = `${name}=${value}; ${expires}; path=/`;
}

function deleteCookie(name){
    setCookie(name, null, null);
}