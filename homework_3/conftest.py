import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_opening():
    browser.config.window_height = 900
    browser.config.window_width = 900
    browser.open('https://google.com')

    yield
    browser.quit()
    print("Браузер закрыт")
