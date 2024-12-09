import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2"

# Функции и тесты для сущности store (Магазин)
# Функция для создания заказа
def create_order(order):
    response = requests.post(f"{BASE_URL}/store/order", json=order)
    return response

# Тест создания заказа
# Ожидаемый результат: Код ответа 200 ОК, заказ создан, id заказов в ответе совпадают с переданными id заказа
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
    response = requests.get(f"{BASE_URL}/store/order/{order_id}")
    return response

# Тест получения заказа по ID
# Ожидаемый результат: Код ответа 200 ОК, заказ получен, id заказов в ответе совпадают с переданными id заказа
@pytest.mark.parametrize("order_id", [1, 2])
def test_get_order_by_id(order_id):
    response = get_order_by_id(order_id)
    assert response.status_code == 200
    assert response.json()["id"] == order_id

# Функция для удаления заказа по ID
def delete_order_by_id(order_id):
    response = requests.delete(f"{BASE_URL}/store/order/{order_id}")
    return response

# Тест удаления заказа по ID
# Ожидаемый результат: Код ответа 200 ОК, заказ удален
@pytest.mark.parametrize("order_id", [1, 2])
def test_delete_order_by_id(order_id):
    response = delete_order_by_id(order_id)
    assert response.status_code == 200

# Функция для получения инвентаря магазина
def get_inventory():
    response = requests.get(f"{BASE_URL}/store/inventory")
    return response

# Тест получения инвентаря магазина
# Ожидаемый результат: Код ответа 200 ОК, инвентарь получен
def test_get_inventory():
    response = get_inventory()
    assert response.status_code == 200

# Функция для обновления заказа
def update_order(order):
    response = requests.post(f"{BASE_URL}/store/order", json=order)
    return response

# Тест обновления заказа
# Ожидаемый результат: Код ответа 200 ОК, заказ изменен, количество в заказе в ответе совпадает с переданным количеством в заказе
@pytest.mark.parametrize("order", [
    {"id": 1, "petId": 1, "quantity": 3, "shipDate": "2024-09-28T23:40:42.000Z", "status": "delivered", "complete": True}
])
def test_update_order(order):
    response = update_order(order)
    assert response.status_code == 200
    assert response.json()["quantity"] == order["quantity"]
