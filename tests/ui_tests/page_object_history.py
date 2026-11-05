from page_object import MainePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select, WebDriverWait


class PageHistory:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open_calculator(self) -> MainePage:
        from ui_tests.page_object import MainePage
        element = self._driver.find_element(By.ID, "calculator-button")
        element.click()
        return MainePage(self._driver)

    def read_screen(self) -> str:
        element = self._driver.find_element(By.ID, "history-list")
        return element.text.replace("\n", " ")

    def read_history_items(self) -> list[str]:
        texts = self._driver.execute_script(
            """
            return Array.from(
                document.querySelectorAll('#history-list .history__item')
            ).map((element) => element.innerText);
            """
        )
        return [" ".join(text.split()) for text in texts]

    def select_operation(self, operation: str) -> None:
        select = Select(
            self._driver.find_element(By.ID, "history-operation-filter")
        )
        select.select_by_value(operation)

    def wait_for_history_items(
        self, expected: list[str], timeout: float = 5
    ) -> None:
        WebDriverWait(self._driver, timeout).until(
            lambda _: self.read_history_items() == expected
        )

    def click_clean(self) -> None:
        element = self._driver.find_element(By.ID, "clear-history")
        element.click()
    def wait_for_screen(self, expected: str, timeout: float = 5) -> None:
        WebDriverWait(self._driver, timeout).until(
            lambda _: self.read_screen() == expected
        )
