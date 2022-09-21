"""
Module providing checking of network interface's state
"""
import pytest
from switcher import lte
from switcher import wifi


def test_interfaces_active():
    """
    The checking that at least one interface is active
    """
    if wifi.isactive is False:
        assert lte.isactive is True
    elif lte.isactive is False:
        assert wifi.isactive is True
    else:
        wifi.isactive is True
        assert lte.isactive is True


def test_both_interfaces_inactive():
    """
    The checking that excludes the situation when both interfaces are inactive
    """
    with pytest.raises(AssertionError):
        assert wifi.isactive is False and lte.isactive is False
