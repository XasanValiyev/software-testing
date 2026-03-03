from pages.login_page import LoginPage
from pages.account_page import Accounts
from pages.kartoteka import Kartoteka
from pages.create_payment import Payment
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
    
    # accounts = Accounts(page)
    # accounts.account_page()
    # accounts.main_account_flow()

    payments = Payment(page)
    payments.click_payment_tab()
    payments.between_my_acocunts()





   

    

    










   