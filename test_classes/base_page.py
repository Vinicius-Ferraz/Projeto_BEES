from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
import time

class BasePage: 
    def __init__(self, driver:WebDriver):
        self.driver=driver
        
    def get_locator_type(self, locator_type: str):
        type = locator_type.upper()
       
        
    def find(self,locator, locator_type='XPATH') -> WebElement:
        type = locator_type.upper()
        element = None
        if type == 'ID':
            element = self.driver.find_element(By.ID, locator) # type: ignore
        elif type == 'CSS_SELECTOR':
            element = self.driver.find_element(By.CSS_SELECTOR, locator) # type: ignore
        elif type == 'XPATH':
            element = self.driver.find_element(By.XPATH, locator) # type: ignore          
        return element # type: ignore 
    
    def click(self, locator, locator_type='XPATH'):
        element = self.find(locator,locator_type)
        element.click()
        time.sleep(3)
        
    def input(self, data, locator, locator_type):
        element = self.find(locator,locator_type)
        element.send_keys(data)
    