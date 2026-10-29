import pytest

from ui_tests.page_object import MainePage
from ui_tests.test_ui import driver


@pytest.fixture
def open_calculator():
    driver.get("http://localhost:1743")
    return MainePage(driver)
