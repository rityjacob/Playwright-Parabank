import pytest
from playwright.sync_api import Page,expect

# from pages.login_page import LoginPage
# from pages.home_page import HomePage

def test_valid_login(login_page,home_page)->None:

    login_page.Login('Benet','Testben123@')

    home_page.expect_welcome_text()
    expect(home_page.logout_link).to_be_visible()

    home_page.logout()


@pytest.mark.negative
@pytest.mark.parametrize("user, pwd, msg", [
    ("kunjumon", "kj", "The username and password could not be verified."),
    ("", "", "Please enter a username and password."),])

def test_login_errors(login_page, user, pwd, msg) -> None:
    login_page.Login(user, pwd)
    expect(login_page.error_message).to_contain_text(msg)