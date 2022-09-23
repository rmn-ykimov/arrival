"""
Module providing checking of network interface's state
"""
import allure

from helper import assert_value
from switcher import wifi, lte, NetworkInterface


@allure.title('Interfaces active')
def test_interfaces_active():
    """
    Checking that at least one interface is active.
    """
    if wifi.is_active is False:
        assert lte.is_active is True
    elif lte.is_active is False:
        assert wifi.is_active is True
    else:
        wifi.is_active is True
        assert lte.is_active is True


@allure.title('Interfaces inactive')
def test_both_interfaces_inactive(get_wifi_object: dict):
    """
    Checking that excludes the situation when both interfaces are inactive.
    """
    wifi: NetworkInterface = get_wifi_object['wifi']
    assert_value(actual_value=wifi.is_active,
                 expected_value=True) and assert_value(
        actual_value=lte.is_active, expected_value=False)
