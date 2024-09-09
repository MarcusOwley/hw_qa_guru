from selene import browser, be, have
import os


def date_generator(day: int, month: int, year: int):
    browser.element('#dateOfBirthInput').click()
    browser.element(f'.react-datepicker__month-select option[value="{month - 1}"]').click()
    browser.element(f'.react-datepicker__year-select option[value="{year}"]').click()
    if day >= 10:
        browser.element(f'.react-datepicker__day.react-datepicker__day--0{day}').click()
    else:
        browser.element(f'.react-datepicker__day.react-datepicker__day--00{day}').click()
def test_fillform():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Marcus')
    browser.element('#lastName').type("Owley")
    browser.element('#userEmail').type('test@test.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('9991235678')
    browser.element('#dateOfBirthInput').click()
    date_generator(5, 12, 1994)

    browser.element('#subjectsInput').type('Compu').press_tab()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('picture.png'))
    browser.element('#currentAddress').type('Place is Unknown')
    browser.element('#react-select-3-input').type('Har').press_tab()
    browser.element('#react-select-4-input').type('Pani').press_tab()
    browser.element('#submit').click()
    ''' После клика на Submit открывается модальное окно (.modal-content) со списком введенных ранее данных.
    Они находятся в ячейках таблицы (которые мы выбираем командой element('table').all('tr').all('td')).
    Командой even мы отфильтровываем значения из четных значений, т.к. именно в них находятся данные
    необходимые нам для проверки (которую мы проводим командой should(have.exact_texts()).
    '''
    assert browser.element('.modal-content').element('table').all('tr').all('td').even.should(have.exact_texts(
        'Marcus Owley',
        'test@test.com',
        'Male',
        '9991235678',
        '05 December,1994',
        'Computer Science',
        'Sports, ' 
        'Reading, ' 
        'Music',
        'picture.png',
        'Place is Unknown',
        'Haryana Panipat'))
