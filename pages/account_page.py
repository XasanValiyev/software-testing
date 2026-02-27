from playwright.sync_api import expect

class Accounts:
    def __init__(self, page):
        self.page = page


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

    def main_account(self):
        self.page.locator(".mantine-1ryt1ht").get_by_text("Barchasi").click()    
        main_account = self.page.locator(".account")
        texts = main_account.all_inner_texts()
        has_main_account = any(t.strip().endswith("001") for t in texts)
        kartoteka_link = self.page.locator('a[href="/kartoteka"]').get_by_text("Kartoteka")
        if has_main_account:
            self.page.locator(".back_btn").click()
            kartoteka = self.page.get_by_role("link", name="Kartoteka").first
            kartoteka.click()
        else:
            self.page.locator(".back_btn").click()
            expect(kartoteka_link).to_have_count(0)