import pytest


@pytest.mark.regression
def test_transfer_funds(login_page, home_page, transfer_page) -> None:

    login_page.Login('Benet', 'Testben123@')

    home_page.goto_transfer_funds()
    transfer_page.transfer('10', '19005', '24333')

    transfer_page.expect_transfer_complete('10.00', '19005', '24333')
    home_page.logout()


@pytest.mark.negative
@pytest.mark.parametrize("amount", ["", "abc"], ids=["empty_amount", "non_numeric_amount"])
def test_transfer_funds_invalid_amount(login_page, home_page, transfer_page, amount) -> None:

    login_page.Login('Benet', 'Testben123@')

    home_page.goto_transfer_funds()
    transfer_page.transfer(amount, '19005', '24333')

    transfer_page.expect_transfer_error()
    home_page.logout()
