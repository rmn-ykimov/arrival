"""
Module that contains network interface switcher's executable code
"""
import os
from config.config import USERNAME, PASSWORD, GOOGLE_DNS, HOST


class NetworkInterface:
    """
    Network interface class
    """
    description = "Describes network interface"

    def __init__(self, name, is_active, traffic_transmission, username, password):
        self.name = name
        self.is_active = is_active
        self.traffic_transmission = traffic_transmission
        self.username = username
        self.password = password

    @classmethod
    def google_response(cls):
        """
        Send ICMP packets to 8.8.8.8
        """
        return os.system("ping -c 60 " + GOOGLE_DNS)

    @classmethod
    def host_response(cls):
        """
        Send ICMP packets to 35.242.186.249
        """
        return os.system("ping -c 60 " + HOST)


wifi = NetworkInterface("wlan1", True, True, USERNAME, PASSWORD)

# Wi-Fi interface's initial state

lte = NetworkInterface("eth3", False, False, None, None)


# LTE interface's initial state

def switching_cycle():
    """
    The function which is describes conditions of switching between wi-fi and lte.
    """
    if wifi.host_response() == 0:
        wifi.traffic_transmission = True
    elif wifi.host_response() != 0:
        while lte.google_response() == 0 and wifi.host_response() != 0:
            lte.is_active = True
            lte.traffic_transmission = True
            wifi.traffic_transmission = False
        else:
            lte.traffic_transmission = False
            lte.is_active = False
            wifi.traffic_transmission = True


switching_cycle()
