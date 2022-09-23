"""
Module providing checking if network interface's credentials are valid
"""
import allure
import pytest
from config.config import USERNAME, PASSWORD
from switcher import NetworkInterface
from switcher import lte
from switcher import wifi


@allure.title('Wi-Fi credentials')
def test_wifi_credentials():
    """
    Checking that username and password for wi-fi are valid.
    """
    assert wifi.username == USERNAME
    assert wifi.password == PASSWORD


@allure.title('LTE credentials')
def test_lte_credentials():
    """
    Checking that lte password and username are valid.
    """
    assert lte.username is None
    assert lte.password is None


@allure.title('Wi-Fi credentials (negative)')
@pytest.mark.xfail()
def test_wifi_credentials_negative():
    """
    Checking that Wi-Fi credentials is not incorrect
    """
    assert wifi.username != USERNAME
    assert wifi.password != PASSWORD


@allure.title('LTE credentials (negative)')
@pytest.mark.xfail()
def test_lte_credentials_negative():
    """
    Checking that LTE credentials is not incorrect
    """
    assert lte.username is not None
    assert lte.password is not None

@allure.title('My test')
def test_wifi_credentials(get_class: dict):
    """Checking that username and password for wi-fi are valid."""
    wifi: NetworkInterface = get_class['wifi']
    assert_value(actual_value=wifi.username, expected_value=USERNAME)
    assert_value(wifi.password, PASSWORD)