import pytest
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait



def test_smoke(main_page):
    pass


@pytest.mark.parametrize(
    ("expression", "expected"),
   [("3 + 5 =",8),
    ("9 - 7 =",2),
    ("5 * 3 =", 15),
    ("9 / 3 =",3)]
)

def test_calculator(expression:str, expected:float,main_page):
    main_page.click_expression(expression)
    WebDriverWait(main_page._driver, 5).until(lambda _: main_page.read_screen() == expected)
    assert expected == main_page.read_screen()


@pytest.mark.parametrize(
    ("expression", "expected"),
   [("3 + 5 =",8),
    ("9 - 7 =",2),
    ("5 * 3 =", 15),
    ("9 / 3 =",3)]
)
def test_calculator_keyboard(expression:str, expected:float,main_page):
    main_page.enter_from_keyboard(expression)
    WebDriverWait(main_page._driver, 5).until(lambda _: main_page.read_screen() == expected)
    assert expected == main_page.read_screen()

def test_open_history(main_page):
    main_page.open_history()
