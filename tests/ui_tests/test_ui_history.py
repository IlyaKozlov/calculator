from ui_tests.page_object import MainePage
from ui_tests.page_object_history import PageHistory


def test_history(main_page: MainePage):
    main_page.click_expression("6 + 5 =")
    history_page: PageHistory = main_page.open_history()
    history_page.wait_for_screen("6 + 5 = 11")
    assert history_page.read_screen() == "6 + 5 = 11"



def test_clean_history(main_page: MainePage):
    main_page.click_expression("8 * 5 =")
    history_page: PageHistory = main_page.open_history()
    history_page.wait_for_screen("8 × 5 = 40")
    history_page.click_clean()
    history_page.wait_for_screen("")
    assert history_page.read_screen() == ""
