from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class MainePageHistory:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open_calculator(self) -> None:
        element = self._driver.find_element(By.ID, "calculator-button")
        element.click()