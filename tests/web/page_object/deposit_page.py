from tests.web.page_object.base_page import BasePage
from selenium.webdriver.common.by import By


class DepositPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    deposit_page_button_locator = '//a[.="Deposits"]'
    new_deposit_button_locator = '/html/body/div/a'
    deposit_name_input_locator = 'deposit_name'
    deposit_address_input_locator = 'deposit_address'
    deposit_city_input_locator = 'deposit_city'
    deposit_state_input_locator = 'deposit_state'
    deposit_zipcode_input_locator = 'deposit_zipcode'
    create_deposit_button_locator = '//*[@id="new_deposit"]/div[2]/input'
    update_deposit_button_locator = '//input[@name="commit"]'
    edit_this_deposit_button_locator = '//a[.="Edit this deposit"]'
    login_successfully_locator = '//p["Signed in successfully"]'
    create_deposit_confirmation_text = '//p[.="Deposit was successfully created."]'
    welcome_to_your_storage_locator = '//h1[.="Welcome to your storage "]'
    destroy_deposit_button_locator = '//button[.="Destroy this deposit"]'
    destroy_deposit_confirmation_text = '//p[.="Deposit was successfully destroyed."]'
    
    @staticmethod
    def get_show_this_deposit_locator(deposit_name):
        return f"//td[contains(text(), '{deposit_name}')]//ancestor::tr//a"

    def navigate_to_deposit(self):
        self.wait(locator=self.welcome_to_your_storage_locator, locator_type=By.XPATH)
        self.click(locator=self.deposit_page_button_locator, locator_type=By.XPATH)

    def submit_new_deposit(self):
        self.click(locator=self.create_deposit_button_locator, locator_type="XPATH")

    def navigate_to_new_deposit(self):
        self.wait(locator=self.new_deposit_button_locator, locator_type=By.XPATH)
        self.click(locator=self.new_deposit_button_locator, locator_type=By.XPATH)

    def input_new_deposit(self,deposit_data):
        self.input(data=deposit_data.get('name', ''), locator=self.deposit_name_input_locator, locator_type=By.ID)
        self.input(data=deposit_data.get('address', ''), locator=self.deposit_address_input_locator, locator_type=By.ID)
        self.input(data=deposit_data.get('city', ''), locator=self.deposit_city_input_locator, locator_type=By.ID)
        self.input(data=deposit_data.get('state', ''), locator=self.deposit_state_input_locator, locator_type=By.ID)
        self.input(data=deposit_data.get('zipcode', ''), locator=self.deposit_zipcode_input_locator, locator_type=By.ID)

    def click_show_this_deposit(self, deposit_name):
        this_deposit = self.get_show_this_deposit_locator(deposit_name)
        self.click(this_deposit, locator_type=By.XPATH)
        
    def click_edit_this_deposit(self):
        self.wait(locator=self.deposit_page_button_locator, locator_type=By.XPATH)
        self.click(self.edit_this_deposit_button_locator, locator_type="XPATH")
    
    def update_deposit_city(self, city):
        self.wait(locator=self.deposit_city_input_locator, locator_type="ID")
        self.input(data=city, locator=self.deposit_city_input_locator, locator_type="ID", clear=True)
        
    def click_update_deposit(self):
        self.wait(locator=self.update_deposit_button_locator, locator_type=By.XPATH)
        self.click(locator=self.update_deposit_button_locator, locator_type="XPATH")

    def get_create_deposit_confirmation_text(self):
        element = self.wait(locator=self.create_deposit_confirmation_text, locator_type=By.XPATH)
        return element.text

    def destroy_deposit(self):
        self.wait(locator=self.destroy_deposit_button_locator, locator_type=By.XPATH)
        self.click(locator=self.destroy_deposit_button_locator, locator_type=By.XPATH)

    def get_destroy_deposit_confirmation_text(self):
        element = self.wait(locator=self.destroy_deposit_confirmation_text, locator_type=By.XPATH)
        return element.text