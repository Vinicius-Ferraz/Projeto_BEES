from selenium import webdriver
from test_classes.base_page import BasePage

class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver
        
    user_email_input_locator = "user_email"
    user_password_input_locator = '//*[@id="user_password"]'
    submit_button_locator = '//*[@id="new_user"]/div[2]/input'
    
    def login(self, email, password):
        self.input(data=email, locator=self.user_email_input_locator, locator_type="ID")
        self.input(data=password, locator=self.user_password_input_locator, locator_type="XPATH")
        self.click(locator=self.submit_button_locator, locator_type="XPATH")
        