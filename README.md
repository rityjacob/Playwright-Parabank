# ParaBank Tests Using Playwright

Automated UI tests for the [ParaBank](https://parabank.parasoft.com/parabank/index.htm) demo banking site, written in Python with Playwright and pytest. Tests use the Page Object Model.

## Project structure

```
pages/              Page objects (locators and actions for each page)
  login_page.py
  home_page.py
tests/              Test files
  conftest.py       Shared pytest fixtures
  test_login_page.py
  test_home_page.py
pytest.ini          pytest settings (import path, test folder, base URL)
requirements.txt    Python dependencies
```

## Setup

Requires Python 3.13 or newer.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install
```

## Running tests

With the virtual environment active, from the project root:

```bash
pytest                          # run all tests
pytest -v                       # show each test by name
pytest tests/test_login_page.py # run one file
pytest -k invalid               # run tests whose name contains "invalid"
pytest --headed                 # show the browser
pytest --headed --slowmo 500    # show the browser, slowed down
pytest --browser firefox        # use another browser (default: chromium)
```

## Notes

- The valid-login test needs a registered ParaBank account. The public demo site resets its data from time to time, so you may need to register the account again.
