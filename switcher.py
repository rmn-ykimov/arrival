"""
Module that contains network interface switcher's executable code
"""
import os
import ip_values
import wifi_credentials


class NetworkInterface:
    """
    Network interface class
    """
    description = "Describes network interface"

    def __init__(self, name, isactive, traffic_transmission, username, password):
        self.name = name
        self.isactive = isactive
        self.traffic_transmission = traffic_transmission
        self.username = username
        self.password = password

    @classmethod
    def google_response(cls):
        """
        Send ICMP packets to 8.8.8.8
        """
        return os.system("ping -c 60 " + ip_values.GOOGLE_DNS)

    @classmethod
    def host_response(cls):
        """
        Send ICMP packets to 35.242.186.249
        """
        return os.system("ping -c 60 " + ip_values.HOST)


wifi = NetworkInterface("wlan1", True, True, wifi_credentials.USERNAME, wifi_credentials.PASSWORD)
"""
Wi-Fi interface's initial state
"""
lte = NetworkInterface("eth3", False, False, None, None)
"""
LTE interface's initial state
"""


def switching():
    """
    The function which is describes conditions of switching between wi-fi and lte.
    """
    if wifi.host_response() == 0:
        wifi.traffic_transmission = True
    elif wifi.host_response() != 0:
        while lte.google_response() == 0 and wifi.host_response() != 0:
            lte.isactive = True
            lte.traffic_transmission = True
            wifi.traffic_transmission = False
        else:
            lte.traffic_transmission = False
            lte.isactive = False
            wifi.traffic_transmission = True


switching()
