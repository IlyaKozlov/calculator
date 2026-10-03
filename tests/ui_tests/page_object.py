from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.common.by import By


class MainePage:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def click_zero(self):
        self._click_button("number-0")

    def click_one(self):
        self._click_button("number-1")

    def click_two(self):
        self._click_button("number-2")

    def click_three(self):
        self._click_button("number-3")

    def click_for(self):
        self._click_button("number-4")

    def click_five(self):
        self._click_button("number-5")

    def click_six(self):
        self._click_button("number-6")

    def click_seven(self):
        self._click_button("number-7")

    def click_eight(self):
        self._click_button("number-8")

    def click_nine(self):
        self._click_button("number-9")

    def click_clear_button(self):
        self._click_button("clear-button")

    def click_backspace_button(self):
        self._click_button("backspace-button")

    def click_divide_button(self):
        self._click_button("divide-button")

    def click_multiply_button(self):
        self._click_button("multiply-button")

    def click_substruct_button(self):
        self._click_button("substruct-button")

    def click_add_button(self):
        self._click_button("add-button")

    def click_equals_button(self):
        self._click_button("equals-button")

    def click_decimal_button(self):
        self._click_button("decimal-button")

    def _click_button(self, id: str):
        element = self._driver.find_element(By.ID, id)
        element.click()

    def read_screen(self) -> float:
        element = self._driver.find_element(By.ID, "display-value")
        return float(element.text)
