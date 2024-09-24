# tests/test_external_api.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from external_api import ExternalAPI
from unittest.mock import patch

@patch('external_api.requests.get')
def test_fetch_inventory(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'Laptop': 5}

    api = ExternalAPI('http://fakeurl.com')
    inventory = api.fetch_inventory()
    assert inventory['Laptop'] == 5
