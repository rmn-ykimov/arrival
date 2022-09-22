"""
Module providing checking if default state of network interface's is valid
"""
import allure

from switcher import lte
from switcher import wifi


@allure.title('Wi-Fi defaults')
def test_wifi_default():
    """
    Checking that default state of wi-fi interface is correct
    """
    assert wifi.name == "wlan1"
    assert wifi.is_active is True
    assert wifi.traffic_transmission is True


@allure.title('LTE defaults')
def test_lte_default():
    """
    Checking that default state of lte interface is correct
    """
    assert lte.name == "eth3"
    assert lte.is_active is False
    assert lte.traffic_transmission is False
