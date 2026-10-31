import pytest
from selenium import webdriver

from ui_tests.page_object import MainePage



@pytest.fixture
def main_page():
    driver = webdriver.Chrome()
    driver.get("http://localhost:1743")
    driver.execute_script("window.sessionStorage.clear();")
    driver.refresh()
    yield MainePage(driver)
    driver.quit()


