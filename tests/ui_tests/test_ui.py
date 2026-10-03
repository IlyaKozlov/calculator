from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from ui_tests.page_object import MainePage

driver = webdriver.Chrome()

def test_smoke():
    driver.get('http://localhost:1743')
    pass

def test_add():
    driver.get('http://localhost:1743')
    page = MainePage(driver)
    page.click_two()
    page.click_add_button()
    page.click_five()
    page.click_equals_button()
    WebDriverWait(driver, 5).until(lambda _: page.read_screen() == 7)
    assert 7 == page.read_screen()
