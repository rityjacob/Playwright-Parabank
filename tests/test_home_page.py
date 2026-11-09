import pytest

from playwright.sync_api import Page,expect

from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_homePage(login_page,home_page)->None:

    login_page.Login('Benet','Testben123@')

    home_page.goto_overview()
    expect(home_page.logout_link).to_be_visible()
    home_page.logout()