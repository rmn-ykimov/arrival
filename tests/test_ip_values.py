"""
Module providing checking of ip addresses validity
"""
import allure
import pytest
from config.config import HOST, GOOGLE_DNS


@allure.title('Google DNS address')
def test_google_dns_address():
    """
    Checking that google dns address is correct
    """
    assert GOOGLE_DNS == "8.8.8.8"


@allure.title('Host address')
def test_host_address():
    """
    Checking that host address is correct
    """
    assert HOST == "35.242.186.249"


@allure.title('Google DNS address (negative)')
@pytest.mark.xfail()
def test_google_dns_address_negative():
    """
    Checking that google dns address is not incorrect
    """
    assert GOOGLE_DNS == "75.222.175.26"


@allure.title('Host address (negative)')
@pytest.mark.xfail()
def test_host_address_negative():
    """
    Checking that host address is not incorrect
    """
    assert HOST == "75.222.175.26"
