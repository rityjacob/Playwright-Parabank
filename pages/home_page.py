from playwright.sync_api import Page,expect


class HomePage:

    def __init__(self, page:Page) -> None:
        self.page = page
        self.logout_link = page.get_by_role("link", name="Log Out")
        self.overview_link = page.get_by_role("link", name="Accounts Overview")


    def logout_visible(self):
        return self.logout_link.is_visible()

    def overview_visible(self):
        self.overview_link.is_visible()
            