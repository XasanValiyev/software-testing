from playwright.sync_api import expect
from pages.navigation import GoBack
from pages.kartoteka import Kartoteka
import allure

class Accounts:
    def __init__(self, page):
        self.page = page
        self.kartoteka = Kartoteka(page)
        self.goback = GoBack(page)

    @allure.step("Check currency")
    def account_page(self):
        
        self.page.locator(".mantine-1ryt1ht").get_by_text("Barcha hisoblar").click()
        self.page.locator(".mantine-1ryt1ht").get_by_text("UZS").click()
        amounts = self.page.locator(".amount")
        for i in range(amounts.count()):
            expect(amounts.nth(i)).to_contain_text("UZS")
        
        self.page.locator(".mantine-1ryt1ht").get_by_text("USD").click()
        amounts = self.page.locator(".amount")
        for i in range(amounts.count()):
            expect(amounts.nth(i)).to_contain_text("USD")

        self.page.locator(".mantine-1ryt1ht").get_by_text("RUB").click()
        amounts = self.page.locator(".amount")
        for i in range(amounts.count()):
            expect(amounts.nth(i)).to_contain_text("RUB")

    @allure.step("Search for a main account ending with 001")
    def main_account(self)->bool:
        self.page.get_by_text("Barchasi").click()
        accounts = self.page.locator(".account")
        texts = accounts.all_inner_texts()
        return any(t.strip().endswith("001") for t in texts)
    

    @allure.step("If main acount open kartoteka page")
    def main_account_flow(self):
        has_main = self.main_account()
        # kartoteka = self.Kartoteka(self, page)
        # goback = self.GoBack(self, page)
        self.goback.go_back()
        self.kartoteka.open_kartoteka_if_available(has_main)
  