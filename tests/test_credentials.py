import wifi_credentials
from switcher import lte
from switcher import wifi


def test_wifi_credentials():
    assert wifi.username == wifi_credentials.username
    assert wifi.password == wifi_credentials.password


def test_lte_credentials():
    assert lte.username == None
    assert lte.password == None