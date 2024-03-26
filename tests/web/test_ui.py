from selenium import webdriver
from page_object.login_page import LoginPage
from page_object.deposit_page import DepositPage
from page_object.item_page import ItemPage
from page_object.inventory_page import InventoryPage
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture(scope="function", autouse=True)
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    base_url = "https://test-bees.herokuapp.com/"
    driver.get(base_url)
    yield driver
    driver.quit()


def login(username, password, driver):
    login_page = LoginPage(driver)
    login_page.login(username, password)
    return login_page


# Login tests
def test_login_successful(driver):
    login_page = login('ferraz.vinicius@gmail.com', '3uM8gKDP59EQpcV', driver)
    assert login_page.get_login_confirmation_text() == "Signed in successfully."


def test_login_unsuccessful_email_required(driver):
    login_page = login('', '3uM8gKDP59EQpcV', driver)
    assert login_page.get_login_unsuccessful_confirmation() == "Login"
    # FIXME - Should be "Email can't be blank"


def test_login_unsuccessful_password_required(driver):
    login_page = login('ferraz.vinicius@gmail.com', '', driver)
    assert login_page.get_login_unsuccessful_confirmation() == "Login"
    # FIXME - Should be "Password can't be blank"


def test_login_unsuccessful_invalid_email(driver):
    login_page = login('ferraz.vinicius', '3uM8gKDP59EQpcV', driver)
    assert login_page.get_login_unsuccessful_confirmation() == "Login"
    # FIXME - Should be "Email is invalid"

def test_forgot_password(driver):
    login_page = LoginPage(driver)
    email = {'email': 'ferraz.vinicius@gmail.com'}
    login_page.click_forgot_password()
    login_page.input_email_forgot_password(email)
    login_page.click_send_reset_password()
    assert login_page.get_password_reset_confirmation() == "Login"


def test_create_new_deposit(driver):
    login('ferraz.vinicius@gmail.com', '3uM8gKDP59EQpcV', driver)
    deposit_data = {'name': 'Deposit novo', 'address': 'Deposit street, 1.a', 'city': 'Campinas', 'state': 'São Paulo', 'zipcode': '13098'}
    deposit_page = DepositPage(driver)
    deposit_page.navigate_to_deposit()
    deposit_page.navigate_to_new_deposit()
    deposit_page.input_new_deposit(deposit_data)
    deposit_page.submit_new_deposit()
    assert deposit_page.get_create_deposit_confirmation_text() == "Deposit was successfully created."
    deposit_page.destroy_deposit()
    assert deposit_page.get_destroy_deposit_confirmation_text() == "Deposit was successfully destroyed."


def test_destroy_deposit_with_item(driver):
    login('ferraz.vinicius@gmail.com', '3uM8gKDP59EQpcV', driver)
    deposit_page = DepositPage(driver)
    deposit_page.navigate_to_deposit()
    deposit_page.click_show_this_deposit_destroy_test()
    deposit_page.destroy_deposit()
    assert deposit_page.get_destroy_deposit_confirmation_text() == "Deposit was successfully destroyed."
    # FIXME - After click in destroy deposit, the pages crashes.


def test_create_new_deposit_without_name(driver):
    login('ferraz.vinicius@gmail.com', '3uM8gKDP59EQpcV', driver)
    deposit_data = {'name': '', 'address': 'Deposit street, 1.a', 'city': 'Campinas', 'state': 'São Paulo', 'zipcode': '13098'}
    deposit_page = DepositPage(driver)
    deposit_page.navigate_to_deposit()
    deposit_page.navigate_to_new_deposit()
    deposit_page.input_new_deposit(deposit_data)
    deposit_page.submit_new_deposit()
    assert deposit_page.get_create_deposit_confirmation_text() == "Deposit was successfully created."
    deposit_page.destroy_deposit()
    assert deposit_page.get_destroy_deposit_confirmation_text() == "Deposit was successfully destroyed."
    # FIXME - Should have mandatory fields


def test_create_new_deposit_without_address(driver):
    login('ferraz.vinicius@gmail.com', '3uM8gKDP59EQpcV', driver)
    deposit_data = {'name': 'Deposit sem endereço', 'address': '', 'city': 'Campinas', 'state': 'São Paulo', 'zipcode': '13098'}
    deposit_page = DepositPage(driver)
    deposit_page.navigate_to_deposit()
    deposit_page.navigate_to_new_deposit()
    deposit_page.input_new_deposit(deposit_data)
    deposit_page.submit_new_deposit()
    assert deposit_page.get_create_deposit_confirmation_text() == "Deposit was successfully created."
    deposit_page.destroy_deposit()
    assert deposit_page.get_destroy_deposit_confirmation_text() == "Deposit was successfully destroyed."
    # FIXME - Should have mandatory fields


def test_create_new_deposit_without_city(driver):
    login('ferraz.vinicius@gmail.com', '3uM8gKDP59EQpcV', driver)
    deposit_data = {'name': 'Deposit sem cidade', 'address': 'Deposit street, 1.a', 'city': '', 'state': 'São Paulo', 'zipcode': '13098'}
    deposit_page = DepositPage(driver)
    deposit_page.navigate_to_deposit()
    deposit_page.navigate_to_new_deposit()
    deposit_page.input_new_deposit(deposit_data)
    deposit_page.submit_new_deposit()
    assert deposit_page.get_create_deposit_confirmation_text() == "Deposit was successfully created."
    deposit_page.destroy_deposit()
    assert deposit_page.get_destroy_deposit_confirmation_text() == "Deposit was successfully destroyed."
    # FIXME - Should have mandatory fields


def test_create_new_deposit_without_state(driver):
    login('ferraz.vinicius@gmail.com', '3uM8gKDP59EQpcV', driver)
    deposit_data = {'name': 'Deposit sem estado', 'address': 'Deposit street, 1.a', 'city': 'Campinas', 'state': '', 'zipcode': '13098'}
    deposit_page = DepositPage(driver)
    deposit_page.navigate_to_deposit()
    deposit_page.navigate_to_new_deposit()
    deposit_page.input_new_deposit(deposit_data)
    deposit_page.submit_new_deposit()
    assert deposit_page.get_create_deposit_confirmation_text() == "Deposit was successfully created."
    deposit_page.destroy_deposit()
    assert deposit_page.get_destroy_deposit_confirmation_text() == "Deposit was successfully destroyed."
    # FIXME - Should have mandatory fields


def test_create_new_deposit_without_zipcode(driver):
    login('ferraz.vinicius@gmail.com', '3uM8gKDP59EQpcV', driver)
    deposit_data = {'name': 'Deposit sem cep', 'address': 'Deposit street, 1.a', 'city': 'Campinas', 'state': 'São Paulo', 'zipcode': ''}
    deposit_page = DepositPage(driver)
    deposit_page.navigate_to_deposit()
    deposit_page.navigate_to_new_deposit()
    deposit_page.input_new_deposit(deposit_data)
    deposit_page.submit_new_deposit()
    assert deposit_page.get_create_deposit_confirmation_text() == "Deposit was successfully created."
    deposit_page.destroy_deposit()
    assert deposit_page.get_destroy_deposit_confirmation_text() == "Deposit was successfully destroyed."
    # FIXME - Should have mandatory fields


def teste_create_new_deposit_blank(driver):
    login('ferraz.vinicius@gmail.com', '3uM8gKDP59EQpcV', driver)
    deposit_data = {'name': '', 'address': '', 'city': '', 'state': '', 'zipcode': ''}
    deposit_page = DepositPage(driver)
    deposit_page.navigate_to_deposit()
    deposit_page.navigate_to_new_deposit()
    deposit_page.input_new_deposit(deposit_data)
    deposit_page.submit_new_deposit()
    assert deposit_page.get_create_deposit_confirmation_text() == "Deposit was successfully created."
    deposit_page.destroy_deposit()
    assert deposit_page.get_destroy_deposit_confirmation_text() == "Deposit was successfully destroyed."
    # FIXME - Should have mandatory fields


def test_edit_deposits(driver):
    login('ferraz.vinicius@gmail.com', '3uM8gKDP59EQpcV', driver)
    deposit_data = {'name': 'Capybara', 'address': 'Deposit_edited', 'city': 'Deposit_edited', 'state': 'Deposit_edited', 'zipcode': 'Deposit_edited'}
    deposit_page = DepositPage(driver)
    deposit_page.navigate_to_deposit()
    deposit_page.click_show_this_deposit()
    deposit_page.click_edit_this_deposit()
    deposit_page.update_deposit_city(deposit_data)
    deposit_page.click_update_deposit()
    assert deposit_page.get_update_deposit_confirmation_text() == "Deposit was successfully updated."


def test_create_new_item(driver):
    login('ferraz.vinicius@gmail.com', '3uM8gKDP59EQpcV', driver)
    item_data = {'name': 'teste_create', 'height': '10', 'width': '10', 'weight': '10'}
    item_page = ItemPage(driver)
    item_page.navigate_to_items_page()
    item_page.click_new_item_button()
    item_page.create_new_item(item_data)
    item_page.submit_new_item()
    assert item_page.get_create_item_confirmation_text() == "Item was successfully created."
    item_page.destroy_item()
    assert item_page.get_destroy_item_confirmation_text() == "Item was successfully destroyed."


def test_create_new_item_without_name(driver):
    login('ferraz.vinicius@gmail.com', '3uM8gKDP59EQpcV', driver)
    item_data = {'name': '', 'height': '10', 'width': '10', 'weight': '10'}
    item_page = ItemPage(driver)
    item_page.navigate_to_items_page()
    item_page.click_new_item_button()
    item_page.create_new_item(item_data)
    item_page.submit_new_item()
    assert item_page.get_create_item_confirmation_text() == "Item was successfully created."
    item_page.destroy_item()
    assert item_page.get_destroy_item_confirmation_text() == "Item was successfully destroyed."


def test_create_new_item_without_height(driver):
    login('ferraz.vinicius@gmail.com', '3uM8gKDP59EQpcV', driver)
    item_data = {'name': 'Item sem altura', 'height': '', 'width': '10', 'weight': '10'}
    item_page = ItemPage(driver)
    item_page.navigate_to_items_page()
    item_page.click_new_item_button()
    item_page.create_new_item(item_data)
    item_page.submit_new_item()
    assert item_page.get_create_item_confirmation_text() == "Item was successfully created."
    item_page.destroy_item()
    assert item_page.get_destroy_item_confirmation_text() == "Item was successfully destroyed."


def test_create_new_item_without_width(driver):
    login('ferraz.vinicius@gmail.com', '3uM8gKDP59EQpcV', driver)
    item_data = {'name': 'Item sem largura', 'height': '10', 'width': '', 'weight': '10'}
    item_page = ItemPage(driver)
    item_page.navigate_to_items_page()
    item_page.click_new_item_button()
    item_page.create_new_item(item_data)
    item_page.submit_new_item()
    assert item_page.get_create_item_confirmation_text() == "Item was successfully created."
    item_page.destroy_item()
    assert item_page.get_destroy_item_confirmation_text() == "Item was successfully destroyed."


def test_create_new_item_blank(driver):
    login('ferraz.vinicius@gmail.com', '3uM8gKDP59EQpcV', driver)
    item_data = {'name': '', 'height': '', 'width': '', 'weight': ''}
    item_page = ItemPage(driver)
    item_page.navigate_to_items_page()
    item_page.click_new_item_button()
    item_page.create_new_item(item_data)
    item_page.submit_new_item()
    assert item_page.get_create_item_confirmation_text() == "Item was successfully created."
    item_page.destroy_item()
    assert item_page.get_destroy_item_confirmation_text() == "Item was successfully destroyed."


# Inventory tests
def test_create_new_inventory(driver):
    login('ferraz.vinicius@gmail.com', '3uM8gKDP59EQpcV', driver)
    item_count = '10'
    inventory_page = InventoryPage(driver)
    inventory_page.navigate_to_inventory_page()
    inventory_page.click_new_inventory_button()
    inventory_page.create_new_inventory(item_count)
    inventory_page.submit_new_iventory()
    assert inventory_page.get_new_inventory_confirmation_text() == "Inventory was successfully created."
    inventory_page.delete_deposit_after_creation()
    assert inventory_page.get_destroy_inventory_confirmation_text() == "Inventory was successfully destroyed."


def test_create_new_inventory_with_taken_item(driver):
    login('ferraz.vinicius@gmail.com', '3uM8gKDP59EQpcV', driver)
    item_count = '10'
    inventory_page = InventoryPage(driver)
    inventory_page.navigate_to_inventory_page()
    inventory_page.click_new_inventory_button()
    inventory_page.create_new_inventory_with_taken_item(item_count)
    inventory_page.submit_new_iventory()
    assert inventory_page.get_item_taken_error() == "Item has already been taken"


def test_create_new_inventory_with_taken_deposit(driver):
    login('ferraz.vinicius@gmail.com', '3uM8gKDP59EQpcV', driver)
    item_count = '10'
    inventory_page = InventoryPage(driver)
    inventory_page.navigate_to_inventory_page()
    inventory_page.click_new_inventory_button()
    inventory_page.create_new_inventory_with_taken_deposit(item_count)
    inventory_page.submit_new_iventory()
    assert inventory_page.get_deposit_taken_error() == "Deposit has already been taken"


def test_create_new_inventory_in_blank(driver):
    login('ferraz.vinicius@gmail.com', '3uM8gKDP59EQpcV', driver)
    inventory_page = InventoryPage(driver)
    inventory_page.navigate_to_inventory_page()
    inventory_page.click_new_inventory_button()
    inventory_page.create_inventory_blank()
    inventory_page.submit_new_iventory()
    assert inventory_page.get_blank_item_error_text() == "Item can't be blank and Item must exist"
    assert inventory_page.get_blank_deposit_error_text() == "Deposit can't be blank and Deposit must exist"


def test_create_new_inventory_without_item(driver):
    login('ferraz.vinicius@gmail.com', '3uM8gKDP59EQpcV', driver)
    item_count = '10'
    inventory_page = InventoryPage(driver)
    inventory_page.navigate_to_inventory_page()
    inventory_page.click_new_inventory_button()
    inventory_page.create_new_inventory_blank_item(item_count)
    inventory_page.submit_new_iventory()
    assert inventory_page.get_blank_item_error_text() == "Item can't be blank and Item must exist"


def test_create_new_inventory_without_deposit(driver):
    login('ferraz.vinicius@gmail.com', '3uM8gKDP59EQpcV', driver)
    item_count = '10'
    inventory_page = InventoryPage(driver)
    inventory_page.navigate_to_inventory_page()
    inventory_page.click_new_inventory_button()
    inventory_page.create_new_inventory_blank_deposit(item_count)
    inventory_page.submit_new_iventory()
    assert inventory_page.get_blank_deposit_error_text() == "Deposit can't be blank and Deposit must exist"


def test_edit_inventory(driver):
    login('ferraz.vinicius@gmail.com', '3uM8gKDP59EQpcV', driver)
    item_count = '405'
    inventory_page = InventoryPage(driver)
    inventory_page.navigate_to_inventory_page()
    inventory_page.click_show_this_inventory()
    inventory_page.click_edit_this_inventory()
    inventory_page.update_this_inventory(item_count)
    assert inventory_page.get_update_confirmation_text() == "Inventory was successfully updated."

