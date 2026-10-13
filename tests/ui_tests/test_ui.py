import pytest
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from ui_tests.page_object import MainePage

driver = webdriver.Chrome()

def test_smoke():
    driver.get('http://localhost:1743')
    pass


@pytest.mark.parametrize(
    ("expression", "expected"),
   [("3 + 5 =",8),
    ("9 - 7 =",2),
    ("5 * 3 =", 15),
    ("9 / 3 =",3)]
)

def test_calculator(expression:str, expected:float):
    driver.get("http://localhost:1743")
    page = MainePage(driver)
    page.click_expression(expression)
    WebDriverWait(driver, 5).until(lambda _: page.read_screen() == expected)
    assert expected == page.read_screen()

