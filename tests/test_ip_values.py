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
@pytest.mark.parametrize('ip', ["75.222.175.26", "67.232.15.87",
                                "57.212.12.94", "87.112.14.64"])
def test_google_dns_negative(ip):
    """
    Checking that google dns address is not incorrect.
    """
    assert GOOGLE_DNS != ip


@allure.title('Host address (negative)')
@pytest.mark.parametrize('ip', ["75.222.175.26", "67.232.15.87",
                                "57.212.12.94", "87.112.14.64"])
def test_host_address_negative(ip):
    """
    Checking that host address is not incorrect.
    """
    assert HOST != ip
