from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class PageHistory:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open_calculator(self) -> "MainePage":
        from ui_tests.page_object import MainePage
        element = self._driver.find_element(By.ID, "calculator-button")
        element.click()
        return MainePage(self._driver)

    def read_screen(self) -> str:
        element = self._driver.find_element(By.ID, "history-list")
        return element.text.replace("\n"," ")

    def click_clean(self) -> None:
        element = self._driver.find_element(By.ID, "clear-history")
        element.click()