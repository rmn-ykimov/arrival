"""
Module providing checking of network interface's state
"""
import allure
import pytest

from switcher import wifi, lte


@allure.title('Interfaces active')
def test_interfaces_active():
    """
    Checking that at least one interface is active
    """
    if wifi.is_active is False:
        assert lte.is_active is True
    elif lte.is_active is False:
        assert wifi.is_active is True
    else:
        wifi.is_active is True
        assert lte.is_active is True


@allure.title('Interfaces inactive')
def test_both_interfaces_inactive():
    """
    Checking that excludes the situation when both interfaces are inactive
    """
    with pytest.raises(AssertionError):
        assert wifi.is_active is False and lte.is_active is False
