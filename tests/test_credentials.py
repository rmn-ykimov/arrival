"""
Module providing checking if network interface's credentials are valid
"""
import pytest
import wifi_credentials
from switcher import lte
from switcher import wifi


def test_wifi_credentials():
    """
    Checking that username and password for wi-fi are valid.
    """
    assert wifi.username == wifi_credentials.USERNAME
    assert wifi.password == wifi_credentials.PASSWORD


# Checking that lte password and username are valid.
def test_lte_credentials():
    """
    Checking that lte password and username are valid.
    """
    assert lte.username is None
    assert lte.password is None


@pytest.mark.xfail()
def test_wifi_credentials_negative():
    """
    Checking that Wi-Fi credentials is not incorrect
    """
    assert wifi.username != wifi_credentials.USERNAME
    assert wifi.password != wifi_credentials.PASSWORD


@pytest.mark.xfail()
def test_lte_credentials_negative():
    """
    Checking that LTE credentials is not incorrect
    """
    assert lte.username is not None
    assert lte.password is not None
