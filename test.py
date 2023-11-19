import requests


def signup_test():
    base_url = "http://localhost:8000/auth/signup/"

    user_data = {
        'username': 'testuser7',
        'email': 'testusers@example.com',
        'password1': 'testpasswor',
        'password2': 'testpasswor',

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
        print("Failed to create a user. Status code:", response.status_code)

signup_test()

def create_transaction_test():

    base_url = "http://localhost:8000/"

    user_data = {
        'amount': 100,
        'date': '2023-11-07',
        'description': 'transactionmoney',
        'category': 2,
        'user': 2

    }

    response = requests.post(base_url, data=user_data)
    print(response.json())
    print(response.status_code)

import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

def history_transactions():

    base_url = "http://localhost:8000/"

    response = requests.get(base_url)
    
    if response.status_code == 200:
        data = response.json()  # Отримуємо дані як словник
        json_data = serializers.serialize('json', data)  # Серіалізуємо словник в JSON
        print(json_data)
    else:
        print("HTTP request failed with status code:", response.status_code)

