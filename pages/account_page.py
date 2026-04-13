from playwright.sync_api import expect
from pages.navigation import GoBack
from pages.kartoteka import Kartoteka
from config.settings import base_api 
import allure

class Accounts:
    def __init__(self, page):
        self.page = page
        self.kartoteka = Kartoteka(page)
        self.goback = GoBack(page)


    # async def navigate(self):
    #     await self.page.goto("{base_url}/currency/list")
        
    @allure.step("Check currency")
    def account_page(self):
        self.page.get_by_text("Barcha hisoblar").click()
        self.page.get_by_role("button", name="UZS").click()
        amounts = self.page.locator(".amount")
        for i in range(amounts.count()):
            expect(amounts.nth(i)).to_contain_text("UZS")
        
        self.page.get_by_role("button", name="USD").click()
        amounts = self.page.locator(".amount")
        for i in range(amounts.count()):
            expect(amounts.nth(i)).to_contain_text("USD")

        self.page.get_by_role("button", name="RUB").click()
        amounts = self.page.locator(".amount")
        for i in range(amounts.count()):
            expect(amounts.nth(i)).to_contain_text("RUB")

    @allure.step("Open currency account")
    def open_account(self):
        self.page.get_by_class(".plus-btn").click()
        self.page.get_by_role("link", name="Hisob raqam ochish").click()
        self.page.wait_for_url("**/currency/rules")
        assert self.page.url == "https://dev-biznes.smartbank.uz/currency/rules"
        assert self.page.get_by_role("button", name="Arizani bankka jo'natish").is_disabled()
        self.page.get_by_role("button", name="Valyuta hisob raqami ochish").click()
        self.page.get_by_role("checkbox", name="RUB").click()
        assert self.page.get_by_role("button", name="Arizani bankka jo'natish").is_enabled()
        self.page.get_by_role("link", "Orqaga").click()
        self.page.get_by_role("link", "Orqaga").click()
        self.page.get_by_role("link", "Orqaga").click()


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
  