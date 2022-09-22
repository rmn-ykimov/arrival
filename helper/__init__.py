import allure


@allure.step('Проверка значения')
def assert_value(actual_value: [str, bool], expected_value: [str, bool]):
    """
    Check my value

    :param actual_value: это какое то значение
    :param expected_value: это еще какое то значение
    """
    if isinstance(actual_value, bool):
        assert actual_value is expected_value, (f'Неверное {actual_value=}, '
                                                f'ожидается {expected_value}')
    else:
        assert actual_value == expected_value, (f'Неверное {actual_value=}, '
                                               f'ожидается {expected_value}')