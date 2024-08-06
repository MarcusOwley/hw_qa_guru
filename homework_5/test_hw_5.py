from selene import browser, be, have
import os

def test_fillform():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Marcus')
    browser.element('#lastName').type("Owley")
    browser.element('#userEmail').type('test@test.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('9991235678')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select option[value="11"]').click()
    browser.element('.react-datepicker__year-select option[value="1994"]').click()
    browser.element('.react-datepicker__day.react-datepicker__day--021').click()
    browser.element('#subjectsInput').type('Compu').press_tab()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('picture.png'))
    browser.element('#currentAddress').type('Place is Unknown')
    browser.element('#react-select-3-input').type('Har').press_tab()
    browser.element('#react-select-4-input').type('Pani').press_tab()
    browser.element('#submit').click()

    assert browser.element('.modal-content').element('table').all('tr').all('td').even.should(have.exact_texts(
        'Marcus Owley',
        'test@test.com',
        'Male',
        '9991235678',
        '21 December,1994',
        'Computer Science',
        'Sports, ' 
        'Reading, ' 
        'Music',
        'picture.png',
        'Place is Unknown',
        'Haryana Panipat'))
