from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_locator_type(self, locator_type: str):
        type = locator_type.upper()

    def find(self, locator, locator_type=By.XPATH) -> WebElement:
        type = locator_type.upper()
        element = None
        if type == 'ID':
            element = self.driver.find_element(By.ID, locator)  # type: ignore
        elif type == 'CSS_SELECTOR':
            element = self.driver.find_element(By.CSS_SELECTOR, locator)  # type: ignore
        elif type == 'XPATH':
            element = self.driver.find_element(By.XPATH, locator)  # type: ignore
        return element  # type: ignore

    def click(self, locator, locator_type=By.XPATH):
        element = self.find(locator, locator_type)
        element.click()

    def input(self, data, locator, locator_type, clear: bool = False):
        element = self.find(locator, locator_type)
        if clear:
            element.clear()
        element.send_keys(data)

    def wait(self, locator, locator_type, timeout=10, poll_frequency=0.5) -> WebElement:
        wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency)
        element = wait.until(EC.presence_of_element_located((locator_type, locator)))
        return element

    #def dropdown_select(self, locator, locator_type, value):
    #    element = self.find(locator, locator_type)
    #    select = Select(element)
    #    select.select_by_visible_text(value)
    #    self.click(select)

    def dropdown_select(self, locator, locator_type, text):
        element = self.wait_for_element(locator, locator_type)
        select = Select(element)
        if select.is_multiple:
            select.select_by_visible_text(text)
        else:
            select.select_by_visible_text(text)

    def wait_for_element(self, locator, locator_type, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((locator_type, locator)))