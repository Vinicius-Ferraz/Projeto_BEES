from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from test_classes.login_page import LoginPage
from test_classes.deposit_page import DepositPage
import time
import pytest
import unittest



CAMINHO_WEBDRIVER = r"C:\Users\Vinicius Ferraz\OneDrive\Documentos\ChromeDriver\chromedriver-win64\chromedriver-win64\chromedriver.exe"
SERVICE = Service(CAMINHO_WEBDRIVER)
BROWSER = webdriver.Chrome(service=SERVICE)
LINK= "https://test-bees.herokuapp.com/"

def test_login_successful():
    BROWSER.get(LINK)
    login = "ferraz.vinicius@gmail.com"
    password = "3uM8gKDP59EQpcV"
    login_page = LoginPage(BROWSER)  
    login_page.login(login, password)
    
def test_login_unsuccessful_email_required():
    BROWSER.get(LINK)
    login = ""
    password = "3uM8gKDP59EQpcV"
    login_page = LoginPage(BROWSER)  
    login_page.login(login, password)
    
# Criação de depósito

def test_create_new_deposit():               
    name = 'Deposit 1'
    address = 'Deposit street, 1a'
    city = 'Campinas'
    state = 'São Paulo'
    zipcode = '13098-427'
    deposit_page = DepositPage(BROWSER)
    deposit_page.navigate_to_deposit()
    deposit_page.input_new_deposit(name, address, city, state, zipcode)
    deposit_page.submit_new_deposit()
    time.sleep(3)
            

def test_edit_deposits():  
    BROWSER.get(LINK)
    login = "ferraz.vinicius@gmail.com"
    password = "3uM8gKDP59EQpcV"
    login_page = LoginPage(BROWSER)  
    login_page.login(login, password)
    deposit_page = DepositPage(BROWSER)
    deposit_page.navigate_to_deposit()
    deposit_page.click_show_this_deposit(deposit_name="Capybara")
    deposit_page.click_edit_this_deposit()
    deposit_page.update_deposit_city('Edited City')
    deposit_page.click_update_deposit()
    time.sleep(3)


#test_edit_deposits()
#login_successful()
#login_unsuccessful_email_required()