from playwright.sync_api import Page, expect


class TransferPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.title = page.get_by_role("heading", name="Transfer Funds")
        self.amount_input = page.locator("#amount")
        self.from_account = page.locator("#fromAccountId")
        self.to_account = page.locator("#toAccountId")
        self.transfer_button = page.get_by_role("button", name="Transfer")
        self.result_title = page.get_by_role("heading", name="Transfer Complete!")
        self.result_message = page.locator("#showResult")
        self.error_title = page.locator("#showError").get_by_role("heading", name="Error!")
        self.error_message = page.locator("#showError .error")

    def transfer(self, amount: str, from_account: str, to_account: str) -> None:
        expect(self.title).to_be_visible()
        self.amount_input.fill(amount)
        # Account options load in after the page opens; select_option waits for them
        self.from_account.select_option(from_account)
        self.to_account.select_option(to_account)
        self.transfer_button.click()

    def expect_transfer_complete(self, amount: str, from_account: str, to_account: str) -> None:
        expect(self.result_title).to_be_visible()
        expect(self.result_message).to_contain_text(
            f"${amount} has been transferred from account #{from_account} to account #{to_account}."
        )

    def expect_transfer_error(self) -> None:
        expect(self.error_title).to_be_visible()
        expect(self.error_message).to_have_text("An internal error has occurred and has been logged.")
        expect(self.result_title).to_be_hidden()
