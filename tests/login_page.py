from playwright.sync_api import Page,expect

from pages.Login_Page import LoginPage

def test_valid_login(page:Page)->None:

    loginpage = LoginPage()

    username = 'Nunu'
    password = 'Testnunu123@'

    loginpage.LoadPage.load()

    loginpage.Login.fill(username,password)

    loginpage.login_button.click()

    

    