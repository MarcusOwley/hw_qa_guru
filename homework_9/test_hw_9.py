from homework_9.fill_form import ProgramStart
from homework_9.students_list import owley_m


def test_fill_form():
    app = ProgramStart(owley_m)

    app.registration.open().filling_form(owley_m).submit()
    app.result.check_form(owley_m)