"""
Module providing checking if default state of network interface's is valid
"""
import allure

from helper import assert_value
from switcher import NetworkInterface


@allure.title('Wi-Fi defaults')
def test_wifi_defaults(get_wifi_object: dict):
    """
    Checking that default state of Wi-Fi interface is correct.
    """
    wifi: NetworkInterface = get_wifi_object['wifi']
    assert_value(actual_value=wifi.name, expected_value="wlan1")
    assert_value(wifi.is_active, True)
    assert_value(wifi.traffic_transmission, True)


@allure.title('LTE defaults')
def test_lte_defaults(get_lte_object: dict):
    """
    Checking that default state of lte interface is correct.
    """
    lte: NetworkInterface = get_lte_object['lte']
    assert_value(actual_value=lte.name, expected_value="eth3")
    assert_value(lte.is_active, False)
    assert_value(lte.traffic_transmission, False)
