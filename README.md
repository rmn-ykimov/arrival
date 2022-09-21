## Description
The autotests are being stored in folder tests in different files, depending on what functionality they reflect.

- [ ] The test_credentials.py includes the autotest cases for [wifi_credentials](wifi_credentials.py)
- [ ] The test_default_interfaces_state.py includes the autotest cases for [default state of Wi-Fi and LTE interfaces](switcher.py)
- [ ] The test_interfaces_state.py includes the autotest cases for check, whether [interfaces up and down](switcher.py)
- [ ] The test_ip_values.py includes the autotest cases for [ip_values](ip_values.py)

The test subject is the switcher.py modules, such as switcher module itself and related ones.
The scope is to cover critical scenarios of Network Interface Switch.

## Test Plan

- [Network Interface Switch](docs/Network Interface Switch.md)
