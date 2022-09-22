"""
Module providing checking of ip addresses validity
"""
import pytest
import ip_values


def test_google_dns_address():
    """
    Checking that google dns address is correct
    """
    assert ip_values.GOOGLE_DNS == "8.8.8.8"


def test_host_address():
    """
    Checking that host address is correct
    """
    assert ip_values.HOST == "35.242.186.249"


@pytest.mark.xfail()
def test_google_dns_address_negative():
    """
    Checking that google dns address is not incorrect
    """
    assert ip_values.GOOGLE_DNS == "75.222.175.26"


@pytest.mark.xfail()
def test_host_address_negative():
    """
    Checking that host address is not incorrect
    """
    assert ip_values.HOST == "75.222.175.26"
