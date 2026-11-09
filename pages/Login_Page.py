from playwright.sync_api import Page,expect


class LoginPage :

    URL = 'https://parabank.parasoft.com/parabank/index.htm'


    def __init__(self, page:Page) -> None:
        self.page = page
        self.username_input = page.locator('input[name=\"username\"]')
        self.pasword_input=page.locator('input[name=\"password\"]')
        self.login_button = page.get_by_role('button', name = 'Login')


    def LoadPage(self) -> None:
        self.goto(self.URL)

    def Login(self,username : str, password : str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)