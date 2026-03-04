
import allure   
from playwright.sync_api import expect
# from config.settings import


class MyProducts:
    def __init__(self, page):
        self.page = page

    def click_salary_carousell(self):
        salary = self.page.get_by_role("link", name="Ish haqi loyihasi")
        expect(salary).to_be_visible()
        salary.click()

    def click_qr_code_carousell(self):
        qr_code = self.page.get_by_role("link", name="QR kod")
        expect(qr_code).to_be_visible()
        qr_code.click()

    def click_kartoteka_carousell(self):
        kartoteka = self.page.get_by_role("link", name="Kartoteka")
        expect(kartoteka).to_be_visible()
        kartoteka.click()    


















