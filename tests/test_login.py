from pages.login_page import LoginPage
from playwright.sync_api import expect


def test_login(page):
    login = LoginPage(page)

    login.open()
    login.login()
    page.wait_for_load_state("networkidle")
    
    # clicks Later button 
    page.locator("#onesignal-slidedown-cancel-button").click()
    
    # checking tabs_account_currency
    page.locator(".mantine-1ryt1ht").get_by_text("Barcha hisoblar").click()
    page.locator(".mantine-1ryt1ht").get_by_text("UZS").click()
    amounts = page.locator(".amount")
    for i in range(amounts.count()):
        expect(amounts.nth(i)).to_contain_text("UZS")
    
    page.locator(".mantine-1ryt1ht").get_by_text("USD").click()
    amounts = page.locator(".amount")
    for i in range(amounts.count()):
        expect(amounts.nth(i)).to_contain_text("USD")

    page.locator(".mantine-1ryt1ht").get_by_text("RUB").click()
    amounts = page.locator(".amount")
    for i in range(amounts.count()):
        expect(amounts.nth(i)).to_contain_text("RUB")
    
    


   


    

