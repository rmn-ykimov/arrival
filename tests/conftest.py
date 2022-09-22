import allure
import pytest
from config.config import USERNAME, PASSWORD
from switcher import NetworkInterface


@pytest.fixture
@allure.title('Wi-Fi fixture')
def get_class() -> dict:
    """Fixture which"""
    yield {
        'wifi': NetworkInterface("wlan1", True, True, USERNAME, PASSWORD),
        'lte': NetworkInterface("eth3", False, False, None, None)
    }
