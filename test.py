import requests


def signup_test():
    base_url = "http://localhost:8000/auth/signup/"

    user_data = {
        'username': 'testuser4',
<<<<<<< HEAD
        'username': 'testuser5',
        'email': 'testuser@example.com',
        'password1': 'testpassword',
        'password2': 'testpassword',

=======
        'email': 'testuser@example.com',
        'password1': 'testpassword',
        'password2': 'testpassword',
>>>>>>> 49b2d5abfb32e2cbc97dc268c66129195453b95b
    }

    response = requests.post(base_url, data=user_data)

    if response.status_code == 201:
        print("User created successfully.")
        user_id = response.json().get('user_id')
        print(f"User ID: {user_id}")
    elif response.status_code == 400:
        print("Failed to create a user. Validation errors:")
        print(response.json().get('errors'))
    else:
        print("Failed to creat  e a user. Status code:", response.status_code)

signup_test()