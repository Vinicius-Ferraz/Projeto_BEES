from selenium import webdriver
from test_classes.base_page import BasePage

class ItemPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver