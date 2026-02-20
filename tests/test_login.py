from pages.login_page import LoginPage

def test_login(page):
    login = LoginPage(page)

    login.open()
    login.login()
   
    cancel_btn = page.get_by_test_id("onesignal-slidedown-cancel-button")
    if cancel_btn.is_visible():
        cancel_btn.click()
    page.locator(".mantine-1ryt1ht").get_by_text("Barcha hisoblar").click()
    page.locator(".mantine-1ryt1ht").get_by_text("Barchasi").click()
    page.locator(".mantine-1ryt1ht").get_by_text("UZS").click()
    page.locator(".mantine-1ryt1ht").get_by_text("USD").click()
    page.locator(".mantine-1ryt1ht").get_by_text("RUB").click()

