"""
Module providing checking of ip addresses validity
"""
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
