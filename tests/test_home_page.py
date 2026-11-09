from playwright.sync_api import Page,expect

from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_homePage(page:Page)->None:

    loginpage = LoginPage(page)
    homepage = HomePage(page)
    
    loginpage.LoadPage()

    loginpage.Login('Nunu','Testnunu123@')

    homepage.goto_overview()
    homepage.logout_visible()
    homepage.logout()