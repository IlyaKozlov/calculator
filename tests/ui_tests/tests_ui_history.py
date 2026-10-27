
from ui_tests.page_object import MainePage
from ui_tests.page_object_history import PageHistory
from ui_tests.test_ui import driver


def test_history():
    driver.get("http://localhost:1743")
    page = MainePage(driver)
    page.click_expression("6 + 5 =")
    history_page: PageHistory = page.open_history()
    assert history_page.read_screen() == "6 + 5 = 11"

def test_clean_history():
    driver.get("http://localhost:1743")
    page = MainePage(driver)
    page.click_expression("8 * 5 =")
    history_page: PageHistory = page.open_history()
    assert history_page.read_screen() == "8 × 5 = 40"
    history_page.click_clean()
    assert history_page.read_screen() == ""