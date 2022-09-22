import allure
import pytest
from config.config import USERNAME, PASSWORD
from switcher import NetworkInterface


@pytest.fixture
@allure.title('Моя первая фикстура')
def get_class() -> dict:
    """Тут должна быть док стринга с описание фикстуры"""
    yield {
        'wifi': NetworkInterface("wlan1", True, True, USERNAME, PASSWORD),
        'lte': NetworkInterface("eth3", False, False, None, None)
    }