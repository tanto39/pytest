import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2"

# Функции и тесты для сущности user (пользователи)
# Функция создания нового пользователя
def create_user(user_data):
    response = requests.post(f"{BASE_URL}/user", json=user_data)
    return response

# Тест создания нового пользователя
# Ожидаемый результат: Код ответа 200 ОК, пользователь создан
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
# Ожидаемый результат: Код ответа 200 ОК, пользователь получен, имя пользователя в ответе совпадает с переданным именем
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
# Ожидаемый результат: Код ответа 200 ОК, пользователь изменен
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
# Ожидаемый результат: Код ответа 200 ОК, пользователь удален
@pytest.mark.parametrize("username", ["testuser1", "testuser2"])
def test_delete_user(username):
    response = requests.delete(f"{BASE_URL}/user/{username}")
    assert response.status_code == 200

# Функция авторизации пользователя с именем пользователя и паролем
def login_user(username, password):
    response = requests.get(f"{BASE_URL}/user/login", params={"username": username, "password": password})
    return response

# Тест авторизации пользователя с именем пользователя и паролем
# Ожидаемый результат: Код ответа 200 ОК, пользователь авторизован
@pytest.mark.parametrize("username, password", [
    ("testuser1", "password1"),
    ("testuser2", "password2")
])
def test_login_user(username, password):
    response = requests.get(f"{BASE_URL}/user/login", params={"username": username, "password": password})
    assert response.status_code == 200