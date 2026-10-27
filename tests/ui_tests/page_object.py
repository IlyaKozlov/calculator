from selenium.webdriver.remote.webdriver import WebDriver
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

    def click_subtract_button(self):
        self._click_button("subtract-button")

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

    def click_expression(self, expression: str) -> None:
        context = {"1": self.click_one,
                   "2": self.click_two,
                   "3": self.click_three,
                   "4": self.click_for,
                   "5": self.click_five,
                   "6": self.click_six,
                   "7": self.click_seven,
                   "8": self.click_eight,
                   "9": self.click_nine,
                   "0": self.click_zero,
                   "+": self.click_add_button,
                   "-": self.click_subtract_button,
                   "*": self.click_multiply_button,
                   "/": self.click_divide_button,
                   "=": self.click_equals_button,
                   ".": self.click_decimal_button,
                   "c": self.click_clear_button,
                   "<": self.click_backspace_button,
                   }
        for letter in expression:
            if letter.isspace():
                continue
            context[letter]()

    def enter_from_keyboard(self, text):
        body = self._driver.find_element(By.TAG_NAME, "body")
        body.send_keys(text)


    def open_history(self) -> "PageHistory":
        from ui_tests.page_object_history import PageHistory
        element = self._driver.find_element(By.ID, "history-button")
        element.click()
        return PageHistory(self._driver)

