from playwright.sync_api import expect
import allure

class Employee:
    def __init__(self, page):
        self.page = page

    