import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ui_tests.page_object import MainePage


@pytest.fixture
def main_page():
    driver = make_chrome()
    driver.get("http://localhost:1743")
    driver.execute_script("window.sessionStorage.clear();")
    driver.refresh()
    yield MainePage(driver)
    driver.quit()


def make_chrome(headless=True):
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--lang=ru-RU")
    options.set_capability("pageLoadStrategy", "normal")

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(30)
    return driver
