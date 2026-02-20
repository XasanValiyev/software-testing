from config.settings import base_url, otpcode, phone_director, password_director

class LoginPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(base_url)
        
    def login(self):

        self.page.fill("input[placeholder='Telefon raqami']", phone_director)

        self.page.click("button[type='submit']")

        otp_inputs = self.page.locator("input[type='tel']")
        for i in range(len(otpcode)):
            otp_inputs.nth(i).fill(otpcode[i])

        self.page.fill("input[type='password']", password_director)
        self.page.click("button[type='submit']")