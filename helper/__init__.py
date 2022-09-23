import allure


@allure.step('Value checking')
def assert_value(actual_value: [str, bool], expected_value: [str, bool]):
    """
    Network interfaces config values checking

    :param actual_value: Actual config value
    :param expected_value: Expected config value
    """
    if isinstance(actual_value, bool):
        assert actual_value is expected_value, (f'Wrong {actual_value=}, '
                                                f'expected value:'
                                                f' {expected_value}')
    else:
        assert actual_value == expected_value, (f'Correct {actual_value=}, '
                                                f'expected value:'
                                                f' {expected_value}')
