import pytest
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

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

def test_calculator(expression:str, expected:float,open_calculator):
    open_calculator.click_expression(expression)
    WebDriverWait(driver, 5).until(lambda _: open_calculator.read_screen() == expected)
    assert expected == open_calculator.read_screen()


@pytest.mark.parametrize(
    ("expression", "expected"),
   [("3 + 5 =",8),
    ("9 - 7 =",2),
    ("5 * 3 =", 15),
    ("9 / 3 =",3)]
)
def test_calculator_keyboard(expression:str, expected:float,open_calculator):
    open_calculator.enter_from_keyboard(expression)
    WebDriverWait(driver, 5).until(lambda _: open_calculator.read_screen() == expected)
    assert expected == open_calculator.read_screen()

def test_open_history(open_calculator):
    open_calculator.open_history()
