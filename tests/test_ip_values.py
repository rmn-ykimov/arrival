import ip_values


def test_google_dns_address():
    assert ip_values.google_dns == "8.8.8.8"


def test_host_address():
    assert ip_values.host == "35.242.186.249"
