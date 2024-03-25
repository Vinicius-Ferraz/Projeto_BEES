from tests.web.page_object.base_page import BasePage
from selenium.webdriver.common.by import By
class ItemPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    # Locators:

    items_page_button_locator = '//a[.="Items"]'
    new_item_button_locator = '//a[.="New item"]'
    new_item_tittle_confirmation_locator = '//h1[.="New item"]'
    input_name_new_item_locator = '//*[@id="item_name"]'
    input_height_new_item_locator = '//*[@id="item_height"]'
    input_width_new_item_locator = '//*[@id="item_width"]'
    input_weight_new_item_locator = '//*[@id="item_weight"]'
    submit_create_item_button_locator = '//*[@value="Create Item"]'
    new_item_created_confirmation_locator = '//p[.="Item was successfully created."]'
    destroy_item_button_locator = '//button[.="Destroy this item"]'
    destroy_item_confirmation_locator = '//p[.="Item was successfully destroyed."]'
    # Methods:

    def navigate_to_items_page(self):
        self.wait(locator=self.items_page_button_locator, locator_type=By.XPATH)
        self.click(locator=self.items_page_button_locator, locator_type=By.XPATH)

    def click_new_item_button(self):
        self.wait(locator=self.new_item_button_locator, locator_type=By.XPATH)
        self.click(locator=self.new_item_button_locator, locator_type=By.XPATH)

    def destroy_item(self):
        self.wait(locator=self.destroy_item_button_locator, locator_type=By.XPATH)
        self.click(locator=self.destroy_item_button_locator, locator_type=By.XPATH)

    def get_destroy_item_confirmation_text(self):
        element = self.wait(locator=self.destroy_item_confirmation_locator, locator_type=By.XPATH)
        return element.text

    def create_new_item(self,item_data):
        self.wait(locator=self.new_item_tittle_confirmation_locator, locator_type=By.XPATH)
        self.input(data=item_data.get('name', ''), locator=self.input_name_new_item_locator, locator_type=By.XPATH)
        self.input(data=item_data.get('height', ''), locator=self.input_height_new_item_locator, locator_type=By.XPATH)
        self.input(data=item_data.get('width', ''), locator=self.input_width_new_item_locator, locator_type=By.XPATH)
        self.input(data=item_data.get('weight', ''), locator=self.input_weight_new_item_locator, locator_type=By.XPATH)

    def submit_new_item(self):
        self.wait(locator=self.submit_create_item_button_locator, locator_type=By.XPATH)
        self.click(locator=self.submit_create_item_button_locator, locator_type=By.XPATH)

    def get_create_item_confirmation_text(self):
        element = self.wait(locator=self.new_item_created_confirmation_locator, locator_type=By.XPATH)
        return element.text
