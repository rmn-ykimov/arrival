import os
import ip_values
import wifi_credentials


# Class which is describes name, state of device (on or off), username, password and if the traffic transmission is
# active of network interface. This class also contains functions for google_dns and host ping.
class NetworkInterface:
    def __init__(self, name, isactive, traffic_transmission, username, password):
        self.name = name
        self.isactive = isactive
        self.traffic_transmission = traffic_transmission
        self.username = username
        self.password = password

    @classmethod
    def google_response(cls):
        return os.system("ping -c 60 " + ip_values.google_dns)

    @classmethod
    def host_response(cls):
        return os.system("ping -c 60 " + ip_values.host)


# Objects of the class (wi-fi and lte) and its initial state
wifi = NetworkInterface("wlan1", True, True, wifi_credentials.username, wifi_credentials.password)
lte = NetworkInterface("eth3", False, False, None, None)


# The function which is describes conditions of switching between wi-fi and lte.
def switching():
    if wifi.host_response() == 0:
        wifi.traffic_transmission = True
    elif wifi.host_response() != 0:
        if lte.google_response() == 0 and wifi.host_response() != 0:
            lte.isactive = True
            lte.traffic_transmission = True
            wifi.traffic_transmission = False
        else:
            lte.traffic_transmission = False
            lte.isactive = False
            wifi.traffic_transmission = True
