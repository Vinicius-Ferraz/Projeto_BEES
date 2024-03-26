from tests.web.page_object.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    user_email_input_locator = "user_email"
    user_password_input_locator = '//*[@id="user_password"]'
    submit_button_locator = '//*[@name="commit"]'
    login_successful_confirm_locator = '//p[.="Signed in successfully."]'
    login_unsuccessful_confirm_locator = '/html/body/div/h2'
    forgot_password_link_locator = '//a[.="Forgot your password?"]'
    forgot_password_title_locator = '//h2[.="Forgot your password?"]'
    email_input_forgot_password_locator = '//*[@id="user_email"]'
    send_reset_password_button_locator = '//*[@name="commit"]'
    get_password_reset_confirmation_locator = '//h2[.="Login"]'

    def login(self, email, password):
        self.input(data=email, locator=self.user_email_input_locator, locator_type="ID")
        self.input(data=password, locator=self.user_password_input_locator, locator_type="XPATH")
        self.click(locator=self.submit_button_locator, locator_type="XPATH")

    def get_login_confirmation_text(self):
        element = self.wait(locator=self.login_successful_confirm_locator, locator_type=By.XPATH)
        return element.text

    def get_login_unsuccessful_confirmation(self):
        element = self.wait(locator=self.login_unsuccessful_confirm_locator, locator_type=By.XPATH)
        return element.text

    def click_forgot_password(self):
        self.wait(locator=self.submit_button_locator, locator_type=By.XPATH)
        self.click(locator=self.forgot_password_link_locator, locator_type=By.XPATH)

    def input_email_forgot_password(self, email):
        self.wait(locator=self.email_input_forgot_password_locator, locator_type=By.XPATH)
        self.input(data=email.get('email', ''), locator=self.email_input_forgot_password_locator, locator_type=By.XPATH)

    def click_send_reset_password(self):
        self.wait(locator=self.send_reset_password_button_locator, locator_type=By.XPATH)
        self.click(locator=self.send_reset_password_button_locator, locator_type=By.XPATH)

    def get_password_reset_confirmation(self):
        element = self.wait(locator=self.get_password_reset_confirmation_locator, locator_type=By.XPATH)
        return element.text
