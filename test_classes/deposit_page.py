from selenium import webdriver
from test_classes.base_page import BasePage

class DepositPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        
        
    deposit_page_button_locator = '//*[@id="navbarSupportedContent"]/ul/li[1]/a'
    new_deposit_button_locator = '/html/body/div/a'
    deposit_name_input_locator = 'deposit_name'
    deposit_address_input_locator = 'deposit_address'
    deposit_city_input_locator = 'deposit_city'
    deposit_state_input_locator = 'deposit_state'
    deposit_zipcode_input_locator = 'deposit_zipcode'
    create_deposit_button_locator = '//*[@id="new_deposit"]/div[2]/input'
    
    def new_deposit(self, name, adress, city, state, zipcode):       
        self.click(locator=self.deposit_page_button_locator, locator_type="XPATH")
        self.click(locator=self.new_deposit_button_locator, locator_type="XPATH")
        self.input(data=name, locator=self.deposit_name_input_locator, locator_type="ID")
        self.input(data=adress, locator=self.deposit_address_input_locator, locator_type="ID")
        self.input(data=city, locator=self.deposit_city_input_locator, locator_type="ID")
        self.input(data=state, locator=self.deposit_state_input_locator, locator_type="ID")
        self.input(data=zipcode, locator=self.deposit_zipcode_input_locator, locator_type="ID")
        self.click(locator=self.create_deposit_button_locator, locator_type="XPATH")