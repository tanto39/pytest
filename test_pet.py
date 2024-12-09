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
# Ожидаемый результат: Код ответа 200 ОК, питомец создан, данные в ответе совпадают с переданными данными
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
# Ожидаемый результат: Код ответа 200 ОК, питомец получен, id питомцев в ответе равен переданным id
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
# Ожидаемый результат: Код ответа 200 ОК, питомец изменен, данные в ответе совпадают с переданными данными
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
# Ожидаемый результат: Код ответа 200 ОК, питомец удален
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
# Ожидаемый результат: Код ответа 200 ОК, питомец изменен, статусы в ответе совпадают с переданными статусами
@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_find_pets_by_status(status):
    response = find_pets_by_status(status)
    assert response.status_code == 200
    assert all(pet["status"] == status for pet in response.json())