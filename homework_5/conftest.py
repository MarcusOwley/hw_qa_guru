import pytest
from selene import browser


@pytest.fixture(scope="session", autouse=True)
def browser_opening():
    browser.config.window_height = 900
    browser.config.window_width = 900
    browser.config.base_url = 'https://demoqa.com'

    yield
    browser.quit()
    print("Браузер закрыт")