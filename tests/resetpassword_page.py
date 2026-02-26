from pages.login_page import LoginPage

def test_login(page):
    login = LoginPage(page)

    login.open()
    login.login()


    page.get_by_text("Parolni unutdingizmi?").click()
