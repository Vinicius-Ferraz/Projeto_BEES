from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from test_classes.login_page import LoginPage
from test_classes.deposit_page import DepositPage
import time

caminho_webdriver = r"C:\Users\Vinicius Ferraz\OneDrive\Documentos\ChromeDriver\chromedriver-win64\chromedriver-win64\chromedriver.exe"

service = Service(caminho_webdriver)

# Inicia o navegador
browser = webdriver.Chrome(service=service)
#browser = webdriver.Chrome(executable_path=caminho_webdriver)

Link= "https://test-bees.herokuapp.com/"

def login_successful():
    
    browser.get(Link)
    
    login = "ferraz.vinicius@gmail.com"
    password = "3uM8gKDP59EQpcV"
    login_page = LoginPage(browser)  
    login_page.login(login, password)
    

def login_unsuccessful_email_required():
    
    browser.get(Link)
    
    login = ""
    password = "3uM8gKDP59EQpcV"
    login_page = LoginPage(browser)

    
    login_page.login(login, password)
    
# Criação de depósito

def create_new_deposit():
    
    #login_successful()
    
    name = 'Deposit 1'
    address = 'Deposit street, 1a'
    city = 'Campinas'
    state = 'São Paulo'
    zipcode = '13098-427'
    deposit_page = DepositPage(browser)
    
    deposit_page.new_deposit(name, address, city, state, zipcode)
    time.sleep(3)
        

login_successful()

#login_unsuccessful_email_required()

create_new_deposit()