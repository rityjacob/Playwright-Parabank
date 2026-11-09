from playwright.sync_api import Page,expect

from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_valid_login(page:Page)->None:

    loginpage = LoginPage(page)
    homepage = HomePage(page)

    loginpage.LoadPage()

    loginpage.Login('Nunu','Testnunu123@')

    expect(page.locator("#leftPanel")).to_contain_text("Welcome Benet Jibu")
    assert homepage.logout_visible(), "Log Out link must appear after successful login"

def test_empty_creds( page : Page) -> None:
    loginpage = LoginPage(page)
    
    loginpage.LoadPage()
    
    loginpage.Login("","")
    expect(page.locator("#rightPanel")).to_contain_text("Please enter a username and password.")
