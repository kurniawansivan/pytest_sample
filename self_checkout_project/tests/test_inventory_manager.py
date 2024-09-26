# tests/test_inventory_manager.py
import pytest
from unittest.mock import Mock
from inventory_manager import InventoryManager

@pytest.fixture
def setup_inventory():
    return {
        1: {'name': 'Laptop', 'stock': 4},
        2: {'name': 'Mouse', 'stock': 15},
    }

def test_restock_when_low_stock(setup_inventory):
    api_client = Mock()
    api_client.update_inventory.return_value = True

    inventory_manager = InventoryManager(setup_inventory, api_client)
    result = inventory_manager.update_stock_and_sync(1, 10)
    
    api_client.update_inventory.assert_called_with(1, 10)
    assert result is True
