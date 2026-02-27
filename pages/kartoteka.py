from playwright.sync_api import expect
import allure

class Kartoteka:
    def __init__(self, page):
        self.page = page

    def open_kartoteka_if_available(self, main_account):
        kartoteka = self.page.get_by_role("link", name="Kartoteka").filter(has=self.page.locator(":visible")).first
        kartoteka.wait_for(timeout=4000)
        if main_account:
            expect(kartoteka).to_be_visible()
            kartoteka.click()
        else:
            expect(kartoteka).to_have_count(0)
        