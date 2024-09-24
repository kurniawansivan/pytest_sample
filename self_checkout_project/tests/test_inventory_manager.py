# tests/test_inventory_manager.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from inventory_manager import InventoryManager

@pytest.fixture
def setup_inventory():
    return {
        1: {'name': 'Laptop', 'stock': 5},
        2: {'name': 'Mouse', 'stock': 0}
    }

def test_in_stock(setup_inventory):
    manager = InventoryManager(setup_inventory)
    assert manager.is_product_in_stock(1) is True

def test_out_of_stock(setup_inventory):
    manager = InventoryManager(setup_inventory)
    assert manager.is_product_in_stock(2) is False
