# tests/test_recommendation_engine.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from recommendation_engine import RecommendationEngine

@pytest.fixture
def setup_inventory():
    return {
        1: {'name': 'Laptop', 'category': 'Electronics', 'stock': 5},
        2: {'name': 'Mouse', 'category': 'Electronics', 'stock': 10},
        3: {'name': 'Shirt', 'category': 'Clothing', 'stock': 20}
    }

def test_recommend_products(setup_inventory):
    engine = RecommendationEngine(setup_inventory)
    
    # Memindai Laptop, hanya Mouse yang harus direkomendasikan
    recommendations = engine.recommend_products(1)
    assert len(recommendations) == 1
    assert recommendations[0]['name'] == 'Mouse'
