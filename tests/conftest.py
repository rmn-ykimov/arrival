"""
Module providing fixtures for network interfaces
"""
import allure
import pytest

from config.config import USERNAME, PASSWORD
from switcher import NetworkInterface


@pytest.fixture
@allure.title('Wi-Fi fixture')
def get_wifi_object() -> dict:
    """Fixture which describes default Wi-Fi state"""
    return {
        'wifi': NetworkInterface("wlan1", True, True, USERNAME, PASSWORD)
    }


@pytest.fixture
@allure.title('LTE fixture')
def get_lte_object() -> dict:
    """Fixture which describes default LTE state"""
    return {
        'lte': NetworkInterface("eth3", False, False, None, None)
    }
