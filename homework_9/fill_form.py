import calendar
import os

from selene import browser, have

from data.student_data import Student
from homework_9.students_list import hobbies_map


class RegistrationPage:

    def __init__(self, student:Student):
        self.first_name = browser.element('#firstName')
        self.second_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.element(f'[for="gender-radio-{student.gender}"]')
        self.phone_number = browser.element('#userNumber')
        self.subjects = browser.element('#subjectsInput')
        self.picture = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.city = browser.element('#react-select-3-input')
        self.state = browser.element('#react-select-4-input')
        self.summary_card = browser.element('#submit')

    def open(self):
        browser.open('/automation-practice-form')
        return self


    def filling_form(self, student: Student):
        self.first_name.type(student.name)
        self.second_name.type(student.secondname)
        self.email.type(student.email)
        self.gender.click()
        self.phone_number.type(student.phone)
        browser.element('#dateOfBirthInput').click()
        browser.element(f'.react-datepicker__month-select option[value="{student.bday_month - 1}"]').click()
        browser.element(f'.react-datepicker__year-select option[value="{student.bday_year}"]').click()
        if student.bday_day >= 10:
            browser.element(f'.react-datepicker__day.react-datepicker__day--0{student.bday_day}').click()
        else:
            browser.element(f'.react-datepicker__day.react-datepicker__day--00{student.bday_day}').click()
        self.subjects.type(student.subject).press_tab()
        for hobbie in student.hobbies:
            browser.element(f'[for="hobbies-checkbox-{hobbie}"]').click()
        # self.choose_hobbies.click()
        self.picture.send_keys(os.path.abspath(student.pic))
        self.address.type(student.addr)
        self.city.type(student.city).press_tab()
        self.state.type(student.state).press_tab()

        return self

    def submit(self):
        self.summary_card.click()
        return self


class ProfileAssertion:
    def __init__(self):
        self.result = browser.element('.modal-content').element('table').all('tr').all('td')[1::2]

    def check_form(self, student: Student):
        day = f'{student.bday_day:02d}'
        month = f'{calendar.month_name[student.bday_month]}'
        if student.gender == 1:
            gender_name = 'Male'
        else:
            gender_name = 'Female'

        hobbies_str = ', '.join([hobbies_map[hobbie_id] for hobbie_id in student.hobbies])

        assert self.result.should(have.exact_texts(f'{student.name} {student.secondname}',
                                                   student.email,
                                                   gender_name,
                                                   student.phone,
                                                   f'{day} {month},{student.bday_year}',
                                                   student.subject,
                                                   f'{hobbies_str}',
                                                   student.pic,
                                                   student.addr,
                                                   f'{student.city} {student.state}'))

class ProgramStart:
    def __init__(self, student: Student):
        self.registration = RegistrationPage(student)
        self.result = ProfileAssertion()