# tests/test_recommendation_engine.py
import pytest
from recommendation_engine import RecommendationEngine

@pytest.fixture
def setup_inventory():
    return {
        1: {'name': 'Laptop', 'category': 'Electronics', 'stock': 5},
        2: {'name': 'Mouse', 'category': 'Electronics', 'stock': 10},
        3: {'name': 'Shirt', 'category': 'Clothing', 'stock': 20}
    }

@pytest.fixture
def setup_purchase_history():
    return {
        101: [{'product_id': 2, 'quantity': 1}, {'product_id': 3, 'quantity': 1}],  # User 101
        102: [{'product_id': 1, 'quantity': 1}]  # User 102
    }

def test_recommend_products_based_on_history(setup_inventory, setup_purchase_history):
    engine = RecommendationEngine(setup_inventory, setup_purchase_history)
    
    recommendations = engine.recommend_products(1, user_id=101)
    assert len(recommendations) == 2  # Mouse dan Shirt direkomendasikan
    assert recommendations[0]['name'] == 'Mouse'
