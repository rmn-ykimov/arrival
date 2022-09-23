"""
Module providing checking if network interface's credentials are valid
"""
import allure
import pytest

from config.config import USERNAME, PASSWORD
from helper import assert_value
from switcher import NetworkInterface


@allure.title('Wi-Fi credentials')
def test_wifi_credentials(get_wifi_object: dict):
    """
    Checking that username and password for Wi-Fi are valid.
    """
    wifi: NetworkInterface = get_wifi_object['wifi']
    assert_value(actual_value=wifi.username, expected_value=USERNAME)
    assert_value(wifi.password, PASSWORD)


@allure.title('LTE credentials')
def test_lte_credentials(get_lte_object: dict):
    """
    Checking that username and password for LTE are valid.
    """
    lte: NetworkInterface = get_lte_object['lte']
    assert_value(actual_value=lte.username, expected_value=None)
    assert_value(lte.password, None)


@allure.title('Wi-Fi credentials (negative)')
@pytest.mark.xfail
def test_wifi_credentials_negative(get_wifi_object: dict):
    """
    Checking that Wi-Fi credentials is not incorrect.
    """
    wifi: NetworkInterface = get_wifi_object['wifi']
    assert_value(actual_value=wifi.password, expected_value=USERNAME)
    assert_value(wifi.username, PASSWORD)


@allure.title('LTE credentials (negative)')
@pytest.mark.xfail()
def test_lte_credentials_negative(get_lte_object: dict):
    """
    Checking that LTE credentials is not incorrect.
    """
    lte: NetworkInterface = get_lte_object['lte']
    assert_value(actual_value=lte.username, expected_value=USERNAME)
    assert_value(lte.password, PASSWORD)
