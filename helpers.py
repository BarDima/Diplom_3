import requests
from data_faker import get_sign_up_data
import allure
from config import add_user_url, delete_user_url

@allure.step("регистрация пользователя")
def registration_user():
    name, email, password = get_sign_up_data()
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    response = requests.post(add_user_url, json=payload)
    response_data = response.json()
    access_token = response_data["accessToken"]
    return access_token, email, password, name

@allure.step("удаление пользователя")
def delete_user(access_token):
    headers = {
        "Authorization": access_token
    }
    response = requests.delete(delete_user_url, headers=headers)
    return response.json()

