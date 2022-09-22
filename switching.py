"""
The module which is contains switching logic
"""
from switcher import wifi, lte


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
