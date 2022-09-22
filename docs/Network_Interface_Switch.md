# Network Interface Switch Tests

## Description

| Filename              | Purpose or function                                                |
|-----------------------|--------------------------------------------------------------------|
| `switcher.py`         | Module that contains network interface switcher's executable code  |
| `ip_values.py`        | Module that contains the information about target IPs              |
| `wifi_credentials.py` | Module that contains the information about Wi-Fi credentials       |

## Test cases

| Test case name                   | Test case objective                                                    | 
|----------------------------------|------------------------------------------------------------------------|
| test_wifi_credentials            | Checking that username and password for wi-fi are valid                |
| test_lte_credentials             | Checking that lte password and username are valid                      |
| test_wifi_default                | Checking that default state of wi-fi interface is correct              |
| test_lte_default                 | Checking that default state of lte interface is correct                |
| test_interfaces_active           | Checking that at least one interface is active                         |
| test_both_interfaces_inactive    | Checking that excludes the situation when both interfaces are inactive |
| test_google_dns_address          | Checking that google dns address is correct                            |
| test_host_address                | Checking that host address is correct                                  |
| test_google_dns_address_negative | Checking that google dns address is not incorrect                      |
| test_host_address_negative       | Checking that host address is not incorrect                            |

## Autotest Cases

### Test case - test_wifi_credentials
**Test case objective:**

Check the wi-fi credentials on compliance with stored values.

**Test case description:**

Validate variables from wifi_credentials.py.

**Test case steps:**

1. Validate variables from wifi_credentials.py, using `assert`.

**Expected results:**

test_wifi_credentials is passed.

### Test case - test_lte_credentials

**Test case objective:**

Check the lte credentials on compliance with stored values.

**Test case description:**

Validate lte's username and password.

**Test case steps:**

1. Validate variables from lte_credentials.py, using `assert`.

**Expected results:**

test_lte_credentials is passed.

### Test case - test_wifi_default

**Test case objective:**

Check the wi-fi default settings on compliance with default object's ones.

**Test case description:**

Validate wifi's name, power status and if traffic is transmitting.

**Test case steps:**

1. Validate variables from switcher.wifi, using `assert`.

**Expected results:**

  test_wifi_default is passed.

### Test case - test_lte_default

**Test case objective:**

Check the lte default settings on compliance with default object's ones.

**Test case description:**

Validate variables from switcher.wifi.

**Test case steps:**

1. Validate lte's name, power status and if traffic is transmitting using `assert`.

**Expected results:**

test_lte_default is passed.

### Test case - test_interfaces_active

**Test case objective:**

Check if at least one interface is up.

**Test case description:**

Validate the state of network interfaces in following combinations:
- lte up, wifi down
- lte up, wifi up
- lte down, wifi up

**Test case steps:**

1. Validate the state of network interfaces in various combinations thus at least one of the interfaces is up using
`assert`.

**Expected results:**

test_interfaces_active is passed.

### Test case - test_both_interfaces_inactive

**Test case objective:**

Check if both interfaces are not down at the same time.

**Test case description:**

Validate the state of network interfaces in following combination:
- lte is not down, wifi is not down

**Test case steps:**

1. Validate the state of network interfaces in combinations thus none of them are down using `assert`.

**Expected results:**

test_both_interfaces_inactive is passed.

### Test case - test_google_dns_address

**Test case objective:**

Check the Google dns address settings.

**Test case description:**

Validate google dns address.

**Test case steps:**

1. Validate google dns address on compliance with ip_values.GOOGLE_DNS using `assert`.

**Expected results:**

test_google_dns_address is passed.

### Test case - test_host_address

**Test case objective:**

Check the host address settings.

**Test case description:**

Validate host address.

**Test case steps:**

1. Validate host address on compliance with ip_values.HOST using `assert`.

**Expected results:**

test_host_address is passed.

### Test case - test_google_dns_address_negative

**Test case objective:**

Check the Google dns address settings.

**Test case description:**

Validate google dns address. Assert stored IP address with incorrect one.

**Test case steps:**

1. Validate google dns address on compliance with "75.222.175.26" using `assert`.

**Expected results:**

test_google_dns_address_negative is passed.

### Test case - test_host_address_negative

**Test case objective:**

Check the host address settings.

**Test case description:**

Validate host address. Assert stored IP address with incorrect one.

**Test case steps:**

1. Validate host address on compliance with "75.222.175.26" using `assert`.

**Expected results:**

test_host_address_negative is passed.