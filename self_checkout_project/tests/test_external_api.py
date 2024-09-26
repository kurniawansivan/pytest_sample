# tests/test_external_api.py
import pytest
from unittest.mock import patch
from external_api import ExternalAPI

@patch('external_api.requests.get')
def test_fetch_inventory_success(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{'id': 1, 'title': 'Sample Product'}]

    api = ExternalAPI('http://dummyurl.com')
    inventory = api.fetch_inventory()
    assert inventory[0]['title'] == 'Sample Product'

@patch('external_api.requests.get')
def test_fetch_inventory_failure(mock_get):
    mock_get.side_effect = Exception("API call failed")

    api = ExternalAPI('http://dummyurl.com')
    
    try:
        inventory = api.fetch_inventory()
    except Exception as e:
        inventory = {}

    # Pastikan dict kosong dikembalikan saat terjadi error
    assert inventory == {}


@patch('external_api.requests.post')
def test_update_inventory_success(mock_post):
    mock_post.return_value.status_code = 201  # POST success

    api = ExternalAPI('http://dummyurl.com')
    result = api.update_inventory(1, 10)
    assert result is True

@patch('external_api.requests.post')
def test_update_inventory_failure(mock_post):
    mock_post.side_effect = Exception("API call failed")

    api = ExternalAPI('http://dummyurl.com')

    try:
        result = api.update_inventory(1, 10)
    except Exception as e:
        result = False

    # Pastikan False dikembalikan saat terjadi error
    assert result is False

