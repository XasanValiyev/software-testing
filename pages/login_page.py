from config.settings import base_url, otpcode, phone_director, password_director
from playwright.sync_api import expect
import allure

class LoginPage:
    def __init__(self, page):
        self.page = page

    @allure.step("Open login page")
    def open(self):
        self.page.goto(base_url)
    
    @allure.step("Login as director")
    def login(self):

        self.page.fill("input[placeholder='Telefon raqami']", phone_director)
        self.page.click("button[type='submit']")
        otp_inputs = self.page.locator("input[type='tel']")
        for i in range(len(otpcode)):
            otp_inputs.nth(i).fill(otpcode[i])
        self.page.fill("input[type='password']", password_director)
        #self.page.click("button[type='submit']")

    def close_main_modal(self):
        close_modal = self.page.get_by_role("button", name="Bekor qilish")
        expect(close_modal).to_be_visible()
        close_modal.click()

    @allure.step("Changing password")
    def change_password(self):   
        self.page.get_by_text("Parolni unutdingizmi?").click()
        otp_inputs = self.page.locator("input[type='tel']")
        otp_inputs.first.wait_for()
        for i in range(len(otpcode)):
            otp_inputs.nth(i).fill(otpcode[i])
        self.page.get_by_placeholder("Parol namunasi: SmartBank1").fill(password_director)
        self.page.get_by_placeholder("Parolni qayta kiriting").fill(password_director)
        self.page.mouse.wheel(0, 2000)
        self.page.get_by_text('Davom etish').click()
        self.page.fill("input[type='password']", password_director)
        self.page.locator(".mantine-1ryt1ht").get_by_text("Kirish").click()
        # self.page.wait_for_load_state("networkidle")

    @allure.step("closing login notification")
    def close_notification(self):
        close_top_modal = self.page.locator("#onesignal-slidedown-cancel-button")
        expect(close_top_modal).to_be_visible()
        close_top_modal.click()
            
        