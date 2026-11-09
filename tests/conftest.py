import pytest

from playwright.sync_api import Page,expect

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.transfer_page import TransferPage


@pytest.fixture
def login_page(page:Page)-> LoginPage:
    lp = LoginPage(page)
    lp.LoadPage()
    return lp

@pytest.fixture
def home_page(page:Page)-> HomePage:
    return HomePage(page)

@pytest.fixture
def transfer_page(page:Page)-> TransferPage:
    return TransferPage(page)
