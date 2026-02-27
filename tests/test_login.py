from pages.login_page import LoginPage
from pages.account_page import Accounts
from playwright.sync_api import expect


def test_login(page):
    login = LoginPage(page)
    login.open()
    login.login()
    login.close_notification()
    
    accounts = Accounts(page)
    accounts.account_page()
    accounts.main_account()
   
    

    










   