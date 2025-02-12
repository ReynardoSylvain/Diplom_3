import uuid
from faker import Faker
import allure
import requests
import json
import data

from data import Urls

fake = Faker()

@allure.step('Генерация строки с использованием библиотеки Faker')
def generate_fake_string():
    return fake.pystr(min_chars=6, max_chars=8)


@allure.step('Генерация почтового адреса с использованием библиотеки Faker')
def generate_fake_email():
    unique_id_short = uuid.uuid4().hex[:2]
    return f"{unique_id_short}_{fake.email()}"


@allure.step('Регистрируем нового пользователя и возвращаем его данные')
def register_new_user_and_return_user_data():
    user_data = {}
    email = generate_fake_email()
    password = generate_fake_string()
    name = generate_fake_string()

    acc_details = {
        'email': email,
        'password': password,
        'name': name
    }


    response = requests.post(Urls.CREATE_USER_HANDLE, data=acc_details)


    try:
        json_response = response.json()
        if response.status_code == 200:
            user_data = {
                'email': email,
                'password': password,
                'name': name,
                'status_code': response.status_code,
                'json': json_response
            }
    except json.JSONDecodeError:
        user_data = {
            'email': email,
            'password': password,
            'name': name,
            'status_code': response.status_code,
            'json': None
        }
    return user_data


@allure.step('Удаляем пользователя')
def delete_user(access_token):
    headers = {'Authorization': access_token}
    requests.delete(Urls.DELETE_USER_HANDLE, headers=headers)


@allure.step('Создаем заказ')
def create_order(user):
    details = {
        'ingredients': [data.TestIDs.INGREDIENTS_ID]
    }
    headers = {'Authorization': user['json']['accessToken']}
    response = requests.post(Urls.ORDERS_HANDLE, json=details, headers=headers)
    return response