import allure

class Tabs:
    def __init__(self, page):
        self.page = page

    @allure.step("Open main page")
    def main_tab(self):
        main = self.page.locator(".sidebarItem_title").get_by_text("Asosiy")
        main.click()

    @allure.step("Open history page")
    def history_tab(self):
        history = self.page.locator(".sidebarItem_title").get_by_text("Tarix")
        history.click()

    @allure.step("Open myaccounts page")
    def myaccounts_tab(self):
        accounts = self.page.locator(".sidebarItem_title").get_by_text("Mening hisoblarim")
        accounts.click()

    @allure.step("Open reports page")
    def reports_tab(self):
        reports = self.page.locator(".sidebarItem_title").get_by_text("Hisobotlar")
        reports.click()
    
    @allure.step("Open foreign ET page")
    def foreignET_tab(self):
        foreignET = self.page.locator(".sidebarItem_title").get_by_text("Valyuta operatsiyalari")
        foreignET.click()

    @allure.step("Open Profile page")
    def profile_tab(self):
        profile = self.page.locator(".sidebarItem_title").get_by_text("Shaxsiy sahifa")
        profile.click()
    