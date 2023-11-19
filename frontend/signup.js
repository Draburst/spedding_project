document.getElementById("signupForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    const form = event.target;
    const formData = new FormData(form);
    
    fetch('http://localhost:8000/auth/signup', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok.');
        }
        return response.json();
    })
    .then(data => {
        // Handle successful response
        console.log('Success:', data);
    })
    .catch(error => {
        // Handle error
        console.error('Error:', error);
    });
});