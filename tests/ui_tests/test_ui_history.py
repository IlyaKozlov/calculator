from ui_tests.page_object_history import PageHistory


def test_history(open_calculator):
    open_calculator.click_expression("6 + 5 =")
    history_page: PageHistory = open_calculator.open_history()
    history_page.wait_for_screen("6 + 5 = 11")
    assert history_page.read_screen() == "6 + 5 = 11"


def test_clean_history(open_calculator):
    open_calculator.click_expression("8 * 5 =")
    history_page: PageHistory = open_calculator.open_history()
    history_page.wait_for_screen("8 × 5 = 40")
    history_page.click_clean()
    history_page.wait_for_screen("")
    assert history_page.read_screen() == ""
