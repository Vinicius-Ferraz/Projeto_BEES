from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from test_classes.login_page import LoginPage
from test_classes.deposit_page import DepositPage
import pytest


@pytest.fixture(scope="function")
def driver():
    caminho_webdriver = r"C:\Users\Vinicius Ferraz\OneDrive\Documentos\ChromeDriver\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    service = Service(caminho_webdriver)
    driver = webdriver.Chrome(service=service)
    base_url = "https://test-bees.herokuapp.com/"
    driver.get(base_url)
    yield driver
    driver.quit()


def login(username, password, driver):
    login_page = LoginPage(driver)
    login_page.login(username, password)


def test_login_successful(driver):
    login('ferraz.vinicius@gmail.com', '3uM8gKDP59EQpcV', driver)
    login_page = LoginPage(driver)
    confirmation_message = login_page.get_login_confirmation_text()
    assert confirmation_message == "Signed in successfully."



def test_login_unsuccessful_email_required(driver):
    login('', '3uM8gKDP59EQpcV', driver)
    login_page = LoginPage(driver)
    confirmation_message = login_page.get_login_unsuccessful_confirmation()
    assert confirmation_message == "Login"


def test_login_unsuccessful_password_required(driver):
    login('ferraz.vinicius@gmail.com', '', driver)
    login_page = LoginPage(driver)
    confirmation_message = login_page.get_login_unsuccessful_confirmation()
    assert confirmation_message == "Login"

def test_create_new_deposit(driver):
    login('ferraz.vinicius@gmail.com', '3uM8gKDP59EQpcV', driver)
    name = 'Deposit nw'
    address = 'Deposit street, 1.a'
    city = 'Campinas'
    state = 'São Paulo'
    zipcode = '13098-'
    deposit_page = DepositPage(driver)
    deposit_page.navigate_to_deposit()
    deposit_page.input_new_deposit(name, address, city, state, zipcode)
    deposit_page.submit_new_deposit()


def test_edit_deposits(driver):
    login('ferraz.vinicius@gmail.com', '3uM8gKDP59EQpcV', driver)
    deposit_page = DepositPage(driver)
    deposit_page.navigate_to_deposit()
    deposit_page.click_show_this_deposit(deposit_name='Capybara')
    deposit_page.click_edit_this_deposit()
    deposit_page.update_deposit_city('Edited City')
    deposit_page.click_update_deposit()

