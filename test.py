import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2"

# Функции и тесты для сущности pet (питомцы)
# Функция для создания нового питомца
def create_pet(pet_id, name, status):
    url = f"{BASE_URL}/pet"
    payload = {
        "id": pet_id,
        "name": name,
        "status": status
    }
    response = requests.post(url, json=payload)
    return response

# Тест создания нового питомца
@pytest.mark.parametrize("pet_id, name, status", [
    (1, "Doggie", "available"),
    (2, "Kitty", "sold"),
])
def test_create_pet(pet_id, name, status):
    response = create_pet(pet_id, name, status)
    assert response.status_code == 200
    assert response.json()["name"] == name
    assert response.json()["status"] == status

# Функция для получения информации о питомце по ID
def get_pet_by_id(pet_id):
    url = f"{BASE_URL}/pet/{pet_id}"
    response = requests.get(url)
    return response

# Тест получения информации о питомце по ID
@pytest.mark.parametrize("pet_id", [1, 2])
def test_get_pet_by_id(pet_id):
    response = get_pet_by_id(pet_id)
    assert response.status_code == 200
    assert response.json()["id"] == pet_id

# Функция для обновления информации о питомце
def update_pet(pet_id, name, status):
    url = f"{BASE_URL}/pet"
    payload = {
        "id": pet_id,
        "name": name,
        "status": status
    }
    response = requests.put(url, json=payload)
    return response

# Тест обновления информации о питомце
@pytest.mark.parametrize("pet_id, name, status", [
    (1, "DoggieUpdated", "pending"),
    (2, "KittyUpdated", "available"),
])
def test_update_pet(pet_id, name, status):
    response = update_pet(pet_id, name, status)
    assert response.status_code == 200
    assert response.json()["name"] == name
    assert response.json()["status"] == status

# Функция для удаления питомца по ID
def delete_pet(pet_id):
    url = f"{BASE_URL}/pet/{pet_id}"
    response = requests.delete(url)
    return response

# Тест удаления питомца по ID
@pytest.mark.parametrize("pet_id", [1, 2])
def test_delete_pet(pet_id):
    response = delete_pet(pet_id)
    assert response.status_code == 200

# Функция для поиска питомцев по статусу
def find_pets_by_status(status):
    url = f"{BASE_URL}/pet/findByStatus"
    params = {"status": status}
    response = requests.get(url, params=params)
    return response

# Тест поиска питомцев по статусу
@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_find_pets_by_status(status):
    response = find_pets_by_status(status)
    assert response.status_code == 200
    assert all(pet["status"] == status for pet in response.json())


# Функции и тесты для сущности user (пользователи)
# Функция создания нового пользователя
def create_user(user_data):
    response = requests.post(f"{BASE_URL}/user", json=user_data)
    return response

# Тест создания нового пользователя
@pytest.mark.parametrize("user_data", [
    {"id": 1, "username": "testuser1", "firstName": "Test", "lastName": "User", "email": "testuser1@example.com", "password": "password1", "phone": "1234567890", "userStatus": 1},
    {"id": 2, "username": "testuser2", "firstName": "Test", "lastName": "User", "email": "testuser2@example.com", "password": "password2", "phone": "0987654321", "userStatus": 1}
])
def test_create_user(user_data):
    response = requests.post(f"{BASE_URL}/user", json=user_data)
    assert response.status_code == 200

# Функция получения информации о пользователе по имени пользователя
def get_user(username):
    response = requests.get(f"{BASE_URL}/user/{username}")
    return response

# Тест получения информации о пользователе по имени пользователя
@pytest.mark.parametrize("username", ["testuser1", "testuser2"])
def test_get_user(username):
    response = requests.get(f"{BASE_URL}/user/{username}")
    assert response.status_code == 200
    assert response.json()["username"] == username

# Функция обновления информации о пользователе по имени пользователя
def update_user(username, user_data):
    response = requests.put(f"{BASE_URL}/user/{username}", json=user_data)
    return response

# Тест обновления информации о пользователе
@pytest.mark.parametrize("username, user_data", [
    ("testuser1", {"firstName": "Updated", "lastName": "User"}),
    ("testuser2", {"firstName": "Updated", "lastName": "User"})
])
def test_update_user(username, user_data):
    response = requests.put(f"{BASE_URL}/user/{username}", json=user_data)
    assert response.status_code == 200

# Функция удаления пользователя по имени пользователя
def delete_user(username):
    response = requests.delete(f"{BASE_URL}/user/{username}")
    return response

# Тест удаления пользователя по имени пользователя
@pytest.mark.parametrize("username", ["testuser1", "testuser2"])
def test_delete_user(username):
    response = requests.delete(f"{BASE_URL}/user/{username}")
    assert response.status_code == 200

# Функция авторизации пользователя с именем пользователя и паролем
def login_user(username, password):
    response = requests.get(f"{BASE_URL}/user/login", params={"username": username, "password": password})
    return response

# Тест авторизации пользователя с именем пользователя и паролем
@pytest.mark.parametrize("username, password", [
    ("testuser1", "password1"),
    ("testuser2", "password2")
])
def test_login_user(username, password):
    response = requests.get(f"{BASE_URL}/user/login", params={"username": username, "password": password})
    assert response.status_code == 200


# Функции и тесты для сущности store (Магазин)
# Функция для создания заказа
def create_order(order):
    response = requests.post(f"{BASE_URL}/order", json=order)
    return response

# Тест создания заказа
@pytest.mark.parametrize("order", [
    {"id": 1, "petId": 1, "quantity": 1, "shipDate": "2024-09-28T23:40:42.000Z", "status": "placed", "complete": True},
    {"id": 2, "petId": 2, "quantity": 2, "shipDate": "2024-09-28T23:40:42.000Z", "status": "approved", "complete": False}
])
def test_create_order(order):
    response = create_order(order)
    assert response.status_code == 200
    assert response.json()["id"] == order["id"]

# Функция для получения заказа по ID
def get_order_by_id(order_id):
    response = requests.get(f"{BASE_URL}/order/{order_id}")
    return response

# Тест получения заказа по ID
@pytest.mark.parametrize("order_id", [1, 2])
def test_get_order_by_id(order_id):
    response = get_order_by_id(order_id)
    assert response.status_code == 200
    assert response.json()["id"] == order_id

# Функция для удаления заказа по ID
def delete_order_by_id(order_id):
    response = requests.delete(f"{BASE_URL}/order/{order_id}")
    return response

# Тест удаления заказа по ID
@pytest.mark.parametrize("order_id", [1, 2])
def test_delete_order_by_id(order_id):
    response = delete_order_by_id(order_id)
    assert response.status_code == 200

# Функция для получения инвентаря магазина
def get_inventory():
    response = requests.get(f"{BASE_URL}/inventory")
    return response

# Тест получения инвентаря магазина
def test_get_inventory(expected_status_code):
    response = get_inventory()
    assert response.status_code == 200

# Функция для обновления заказа
def update_order(order_id, order):
    response = requests.put(f"{BASE_URL}/order/{order_id}", json=order)
    return response

# Тест обновления заказа
@pytest.mark.parametrize("order_id, order", [
    (1, {"id": 1, "petId": 1, "quantity": 3, "shipDate": "2024-09-28T23:40:42.000Z", "status": "delivered", "complete": True}),
    (2, {"id": 2, "petId": 2, "quantity": 4, "shipDate": "2024-09-28T23:40:42.000Z", "status": "canceled", "complete": False})
])
def test_update_order(order_id, order):
    response = update_order(order_id, order)
    assert response.status_code == 200
    assert response.json()["quantity"] == order["quantity"]
