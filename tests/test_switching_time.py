import wifi_credentials


def test_wifi_credentials():
    assert wifi.username == wifi_credentials.username
    assert wifi.password == wifi_credentials.password



