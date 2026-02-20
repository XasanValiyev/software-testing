from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # headless=True для фона
    page = browser.new_page()
    page.goto("https://biznes.openbank.uz")
    page.expect_response('100')
    page.screenshot(path="screenshot.png")
    browser.close()
    