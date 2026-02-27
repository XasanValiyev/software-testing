import allure


class GoBack:
    def __init__(self, page):
        self.page = page

    def go_back(self):
        self.page.locator(".back_btn").click()
