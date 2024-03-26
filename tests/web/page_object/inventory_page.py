from tests.web.page_object.base_page import BasePage
from selenium.webdriver.common.by import By


class InventoryPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
# Locators:

    inventory_page_button_locator = '//a[.="Inventory"]'
    new_inventory_button_locator = '//a[.="New inventory"]'
    select_item_dropdown_locator = '//*[@id="inventory_item_id"]'
    select_deposit_dropdown_locator = '//*[@id="inventory_deposit_id"]'
    input_quantity_locator = '//*[@id="inventory_item_count"]'
    validation_tittle_new_inventory_page_locator = '/html/body/div/h1'
    create_new_inventory_button_locator = '//*[@id="new_inventory"]/div[2]/input'
    new_inventory_confirmation_text_locator = '//p[.="Inventory was successfully created."]'
    show_this_deposit_locator = '//*[@id="inventories"]/table/tbody/tr[4]/td[4]/a'
    destroy_inventory_button_locator = '//button[.="Destroy this inventory"]'
    edit_this_inventory_button_locator = '//a[.="Edit this inventory"]'
    update_inventory_button_locator = '//input[@name="commit"]'
    update_success_confirmation_locator = '/html/body/div/p'
    error_blank_item_locator = '//*[@id="new_inventory"]/div[2]/div[1]/div'
    error_blank_deposit_locator = '//*[@id="new_inventory"]/div[2]/div[2]/div'
    error_item_already_taken_locator = '//*[@id="new_inventory"]/div[2]/div[1]/div'
    error_deposit_already_taken_locator = '//*[@id="new_inventory"]/div[2]/div[2]/div'
    destroy_inventory_confirmation_text = '//p[.="Inventory was successfully destroyed."]'


# Methods:

    def navigate_to_inventory_page(self):
        self.wait(locator=self.inventory_page_button_locator, locator_type=By.XPATH)
        self.click(locator=self.inventory_page_button_locator, locator_type=By.XPATH)

    def click_new_inventory_button(self):
        self.wait(locator=self.new_inventory_button_locator, locator_type=By.XPATH)
        self.click(locator=self.new_inventory_button_locator, locator_type=By.XPATH)

    def create_new_inventory(self, item_count):
        self.wait(locator=self.validation_tittle_new_inventory_page_locator, locator_type=By.XPATH)
        self.dropdown_select(locator=self.select_item_dropdown_locator, locator_type=By.XPATH, text='Capybara')
        self.dropdown_select(locator=self.select_deposit_dropdown_locator, locator_type=By.XPATH, text='Capybara')
        self.input(data=item_count, locator=self.input_quantity_locator, locator_type=By.XPATH)

    def create_new_inventory_with_taken_item(self, item_count):
        self.wait(locator=self.validation_tittle_new_inventory_page_locator, locator_type=By.XPATH)
        self.dropdown_select(locator=self.select_item_dropdown_locator, locator_type=By.XPATH, text='item_taken')
        self.dropdown_select(locator=self.select_deposit_dropdown_locator, locator_type=By.XPATH, text='Capybara')
        self.input(data=item_count.get('Item count', ''), locator=self.input_quantity_locator, locator_type=By.XPATH)

    def get_item_taken_error(self):
        element = self.wait(locator=self.error_item_already_taken_locator, locator_type=By.XPATH)
        return element.text

    def create_new_inventory_with_taken_deposit(self, item_count):
        self.wait(locator=self.validation_tittle_new_inventory_page_locator, locator_type=By.XPATH)
        self.dropdown_select(locator=self.select_item_dropdown_locator, locator_type=By.XPATH, text='Capybara')
        self.dropdown_select(locator=self.select_deposit_dropdown_locator, locator_type=By.XPATH, text='deposit_taken')
        self.input(data=item_count, locator=self.input_quantity_locator, locator_type=By.XPATH)

    def get_deposit_taken_error(self):
        element = self.wait(locator=self.error_deposit_already_taken_locator, locator_type=By.XPATH)
        return element.text

    def create_inventory_blank(self):
        self.wait(locator=self.validation_tittle_new_inventory_page_locator, locator_type=By.XPATH)

    def create_new_inventory_blank_item(self, item_count):
        self.wait(locator=self.validation_tittle_new_inventory_page_locator, locator_type=By.XPATH)
        self.dropdown_select(locator=self.select_deposit_dropdown_locator, locator_type=By.XPATH, text='Capybara')
        self.input(data=item_count, locator=self.input_quantity_locator, locator_type=By.XPATH)

    def get_blank_item_error_text(self):
        element = self.wait(locator=self.error_blank_item_locator, locator_type=By.XPATH)
        return element.text

    def create_new_inventory_blank_deposit(self, item_count):
        self.wait(locator=self.validation_tittle_new_inventory_page_locator, locator_type=By.XPATH)
        self.dropdown_select(locator=self.select_item_dropdown_locator, locator_type=By.XPATH, text='Capybara')
        self.input(data=item_count, locator=self.input_quantity_locator, locator_type=By.XPATH)

    def get_blank_deposit_error_text(self):
        element = self.wait(locator=self.error_blank_deposit_locator, locator_type=By.XPATH)
        return element.text

    def submit_new_iventory(self):
        self.wait(locator=self.create_new_inventory_button_locator, locator_type=By.XPATH)
        self.click(locator=self.create_new_inventory_button_locator, locator_type=By.XPATH)

    def get_new_inventory_confirmation_text(self):
        element = self.wait(locator=self.new_inventory_confirmation_text_locator, locator_type=By.XPATH)
        return element.text

    def delete_deposit_after_creation(self):
        self.wait(locator=self.destroy_inventory_button_locator, locator_type=By.XPATH)
        self.click(locator=self.destroy_inventory_button_locator, locator_type=By.XPATH)

    def get_destroy_inventory_confirmation_text(self):
        element = self.wait(locator=self.destroy_inventory_confirmation_text, locator_type=By.XPATH)
        return element.text

    def click_show_this_inventory(self):
        self.wait(locator=self.show_this_deposit_locator, locator_type=By.XPATH)
        self.click(locator=self.show_this_deposit_locator, locator_type=By.XPATH)

    def click_edit_this_inventory(self):
        self.wait(locator=self.edit_this_inventory_button_locator, locator_type=By.XPATH)
        self.click(locator=self.edit_this_inventory_button_locator, locator_type=By.XPATH)

    def update_this_inventory(self, item_count):
        self.wait(locator=self.input_quantity_locator, locator_type=By.XPATH)
        self.input(data=item_count, locator=self.input_quantity_locator, locator_type=By.XPATH, clear=True)
        self.click(locator=self.update_inventory_button_locator, locator_type=By.XPATH)

    def get_update_confirmation_text(self):
        element = self.wait(locator=self.update_success_confirmation_locator, locator_type=By.XPATH)
        return element.text


