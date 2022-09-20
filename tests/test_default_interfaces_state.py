from switcher import lte
from switcher import wifi


def test_wifi_default():
    assert wifi.name == "wlan1"
    assert wifi.isactive == True
    assert wifi.traffic_transmission == True


def test_lte_default():
    assert lte.name == "eth3"
    assert lte.isactive == False
    assert lte.traffic_transmission == False
