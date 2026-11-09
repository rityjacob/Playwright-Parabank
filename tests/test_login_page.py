from playwright.sync_api import Page,expect

from pages.login_page import LoginPage

def test_valid_login(page:Page)->None:

    loginpage = LoginPage(page)

    username = 'Nunu'
    password = 'Testnunu123@'

    loginpage.LoadPage()

    loginpage.Login(username,password)

    expect(page.locator("#leftPanel")).to_contain_text("Welcome Benet Jibu")


    

    

    