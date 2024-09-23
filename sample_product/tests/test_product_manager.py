import pytest
import sys
import os

# Menambahkan folder src ke dalam path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from product_manager import ProductManager

@pytest.fixture
def product_manager():
    manager = ProductManager()
    manager.add_product(1, "Laptop", 1500.0, 10)
    manager.add_product(2, "Mouse", 20.0, 50)
    return manager

def test_add_product(product_manager):
    product_manager.add_product(3, "Keyboard", 45.0, 20)
    assert product_manager.products[3]['name'] == "Keyboard"
    assert product_manager.products[3]['price'] == 45.0
    assert product_manager.products[3]['stock'] == 20

def test_add_product_raises_value_error(product_manager):
    with pytest.raises(ValueError):
        product_manager.add_product(1, "Laptop", 1500.0, 10)

def test_check_stock(product_manager):
    stock = product_manager.check_stock(1)
    assert stock == 10

def test_check_stock_raises_key_error(product_manager):
    with pytest.raises(KeyError):
        product_manager.check_stock(999)

@pytest.mark.parametrize("product_id, discount, expected_price", [
    (1, 10, 1350.0),  # 10% diskon dari 1500
    (2, 50, 10.0),    # 50% diskon dari 20
])
def test_apply_discount(product_manager, product_id, discount, expected_price):
    discounted_price = product_manager.apply_discount(product_id, discount)
    assert discounted_price == expected_price

def test_apply_discount_raises_value_error(product_manager):
    with pytest.raises(ValueError):
        product_manager.apply_discount(1, 150)  # Diskon di atas 100% tidak valid
