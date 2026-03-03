import allure
from config.settings import doc_number, summ, textarea_text


class Payment:
    def __init__(self, page):
        self.page = page

    def click_payment_tab(self):
        create_tab = self.page.locator(".create_payment")
        create_tab.click()

    def between_my_acocunts(self):
        self.page.locator(".main_card_title").get_by_text("Hisob raqamlarim o‘rtasida").click()
        self.page.fill("input[placeholder='Hujjat raqami']", doc_number)
        self.page.locator(".currency_input").fill(str(summ))
        self.page.locator("input[type='search']").click()
      
        catalog = self.page.get_by_text("To‘lov kodi", exact=False)
        catalog.wait_for(state="visible")
        catalog.click()

        dropdown = self.page.locator("[role='listbox']")
        dropdown.wait_for(state="visible")
        dropdown.locator("[role='option']").first.click()

        message = self.page.get_by_placeholder("To‘lov maqsadi")
        message.click()
        message.fill(textarea_text)

        btn = self.page.locator(".mantine-Button-inner").get_by_text("Yaratish")
        btn.click()


