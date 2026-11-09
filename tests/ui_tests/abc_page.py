from selenium.webdriver.remote.webdriver import WebDriver


class Page:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def reload(self):
        self._driver.refresh()
        from ui_tests.page_object import MainePage
        return MainePage(self._driver)

