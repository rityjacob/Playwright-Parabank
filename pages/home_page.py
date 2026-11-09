from playwright.sync_api import Page,expect


class HomePage:

    def __init__(self, page:Page) -> None:
        self.page = page
        self.logout_link = page.get_by_role("link", name="Log Out")
        self.overview_link = page.get_by_role("link", name="Accounts Overview")
        self.welcome_text = page.locator("#leftPanel")


    def logout_visible(self):
        return self.logout_link.is_visible()

    def goto_overview(self):
        self.overview_link.click()

    def welcome_text(self):
            self.welcome_text.to_contain_text("Welcome")
    
            