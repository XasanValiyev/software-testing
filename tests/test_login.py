from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    otpcode = '357159'
    browser = p.chromium.launch(headless=False)  # headless=True для фона
    page = browser.new_page()
    page.goto("https://biznes.openbank.uz/login")
    page.expect_response('100')
    # page.screenshot(path="screenshot.png")
    page.fill("input[placeholder='Telefon raqami']", "901340078")
    page.click("button[type='submit']")
    inputs = page.locator("input[type='tel']")
    for i in range(len(otpcode)):
        inputs.nth(i).fill(otpcode[i])





    page.wait_for_timeout(9000)  
    # browser.close()
    