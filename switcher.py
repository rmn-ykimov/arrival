"""
Module that contains network interface switcher's executable code
"""
import os
from config.config import USERNAME, PASSWORD, GOOGLE_DNS, HOST
from switching import switching_cycle


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

switching_cycle()
