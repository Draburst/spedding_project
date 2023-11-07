import requests


def signup_test():
    base_url = "http://localhost:8000/auth/signup/"

    user_data = {
        'username': 'testuser6',
        'email': 'testuser@example.com',
        'password1': 'testpassword',
        'password2': 'testpassword',

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

def create_transaction_test():

    base_url = "http://localhost:8000/"

    user_data = {
        'amount': 10,
        'date': '2023-11-06',
        'description': 'milk',
        'category': 1,
        'user': 1

    }

    response = requests.post(base_url, data=user_data)
    print(response.json())
    print(response.status_code)

create_transaction_test()