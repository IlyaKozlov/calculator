import random

from selenium.webdriver.support.ui import WebDriverWait
from ui_tests.page_object import MainePage
from ui_tests.page_object_history import PageHistory


def test_history(main_page: MainePage):
    main_page.click_expression("6 + 5 =")
    history_page: PageHistory = main_page.open_history()
    history_page.wait_for_screen("6 + 5 = 11")
    assert history_page.read_screen() == "6 + 5 = 11"



def test_filter_for_all_operations(main_page: MainePage):
    operations = [
        ("+", "6 + 5 =", 11, "6 + 5 = 11"),
        ("-", "9 - 4 =", 5, "9 - 4 = 5"),
        ("*", "3 * 7 =", 21, "3 × 7 = 21"),
        ("/", "8 / 2 =", 4, "8 / 2 = 4"),
    ]
    random.shuffle(operations)

    for _, expression, result, _ in operations:
        main_page.click_clear_button()
        main_page.click_expression(expression)
        WebDriverWait(main_page._driver, 5).until(
            lambda _, expected=result: main_page.read_screen() == expected
        )

    history_page: PageHistory = main_page.open_history()

    operation_symbols = {"+": "+", "-": "-", "*": "×", "/": "/"}
    visited_operations = set()

    for operation, _, _, expected_item in operations:
        history_page.select_operation(operation)
        history_page.wait_for_history_items([expected_item])
        filtered_items = history_page.read_history_items()

        assert filtered_items == [expected_item]
        assert all(
            operation_symbols[operation] in item for item in filtered_items
        )
        visited_operations.add(operation)

    assert visited_operations == set(operation_symbols)



def test_clean_history(main_page: MainePage):
    main_page.click_expression("8 * 5 =")
    history_page: PageHistory = main_page.open_history()
    history_page.wait_for_screen("8 × 5 = 40")
    history_page.click_clean()
    history_page.wait_for_screen("")
    assert history_page.read_screen() == ""


