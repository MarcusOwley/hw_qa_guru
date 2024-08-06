from selene import browser, be, have


def test_search_selene():
    browser.element('[name="q"]').should(be.blank).type('windows').press_enter()
    browser.element('[id="search"]').should(have.text('Скачайте дополнения, расширения, пакеты обновления и другие инструменты'))


def test_search_error():
    browser.element('[name="q"]').should(be.blank).type('3453463456734741535').press_enter()
    browser.element('[id="botstuff"]').should(have.text('ничего не найдено'))
