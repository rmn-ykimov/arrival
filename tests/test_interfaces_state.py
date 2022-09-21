import pytest
from switcher import lte
from switcher import wifi


# Checking that at least one interface is active.
def test_interfaces_active():
    if wifi.isactive == False:
        assert lte.isactive == True
    elif lte.isactive == False:
        assert wifi.isactive == True
    else:
        wifi.isactive == True
        assert lte.isactive == True


# Checking that excludes the situation when both interfaces are inactive.
def test_both_interfaces_inactive():
    with pytest.raises(AssertionError):
        assert wifi.isactive == False and lte.isactive == False
