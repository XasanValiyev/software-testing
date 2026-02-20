from playwright.sync_api import sync_playwright
otpcode = '357159'

with sync_playwright() as p:
    
    browser = p.chromium.launch(headless=False) 
    page = browser.new_page()
    page.goto("https://biznes.openbank.uz/login")
    page.screenshot(path="screenshot.png")
    page.fill("input[placeholder='Telefon raqami']", "901340078")
    page.click("button[type='submit']")
    inputs = page.locator("input[type='tel']")
    page.screenshot(path="screenshot.png")
    for i in range(len(otpcode)):
        inputs.nth(i).fill(otpcode[i])
    page.wait_for_timeout(500)   
    page.screenshot(path="screenshot.png")
    page.fill(".mantine-1sihklk", "Smartbank12")
    page.click("button[type='submit']")

    page.click(".logout")
    page.get_by_text("Bekor qilish").click()

    page.wait_for_timeout(500)   

    page.click(".logout")
    page.get_by_text("Tasdiqlash").click()



    page.wait_for_timeout(5000)  
    # browser.close()
    