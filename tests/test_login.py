from pages.login_page import LoginPage
from pages.account_page import Accounts
from pages.kartoteka import Kartoteka
from pages.create_payment import Payment
from pages.tabs_page import Tabs
from pages.products_page import MyProducts
from playwright.sync_api import expect
import allure 


@allure.feature("Accounts")
@allure.title("Verify currency filtering")
def test(page):
    login = LoginPage(page)
    login.open()
    login.login()
    login.change_password()
    login.close_notification()
    login.close_main_modal()
    
    tabs = Tabs(page)
    tabs.main_tab()
    tabs.history_tab()
    tabs.myaccounts_tab()
    tabs.reports_tab()
    tabs.foreignET_tab()
    tabs.profile_tab()

    tabs.main_tab()
    accounts = Accounts(page)
    accounts.account_page()
    accounts.main_account_flow()

    payments = Payment(page)
    payments.click_payment_tab()
    payments.between_my_acocunts()

    products = MyProducts(page)
    products.click_salary_carousell()
    tabs.main_tab()
    products.click_qr_code_carousell()
    tabs.main_tab()
    products.click_kartoteka_carousell()
    









   

    

    










   