from test_classes.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    user_email_input_locator = "user_email"
    user_password_input_locator = '//*[@id="user_password"]'
    submit_button_locator = '//*[@id="new_user"]/div[2]/input'
    login_successful_confirm_locator = '//p[.="Signed in successfully."]'
    login_unsuccessful_confirm_locator = '/html/body/div/h2'

    def login(self, email, password):
        self.input(data=email, locator=self.user_email_input_locator, locator_type="ID")
        self.input(data=password, locator=self.user_password_input_locator, locator_type="XPATH")
        self.click(locator=self.submit_button_locator, locator_type="XPATH")

    def get_login_confirmation_text(self):
        element = self.wait(locator=self.login_successful_confirm_locator, locator_type="XPATH")
        return element.text

    def get_login_unsuccessful_confirmation(self):
        element = self.wait(locator=self.login_unsuccessful_confirm_locator, locator_type="XPATH")
        return element.text