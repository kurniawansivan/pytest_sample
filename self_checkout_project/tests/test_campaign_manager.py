# tests/test_campaign_manager.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from campaign_manager import CampaignManager

@pytest.fixture
def setup_campaigns():
    campaigns = [
        {'name': 'Summer Sale', 'start_time': 10, 'end_time': 20},
        {'name': 'Winter Sale', 'start_time': 21, 'end_time': 30}
    ]
    return CampaignManager(campaigns)

def test_active_campaign(setup_campaigns):
    current_time = 15
    campaign = setup_campaigns.get_active_campaign(current_time)
    assert campaign['name'] == 'Summer Sale'

def test_no_active_campaign(setup_campaigns):
    current_time = 35
    campaign = setup_campaigns.get_active_campaign(current_time)
    assert campaign is None
