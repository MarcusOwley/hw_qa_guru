import dataclasses


@dataclasses.dataclass
class Student:
    name: str
    secondname: str
    email: str
    phone: str
    subject: str
    addr: str
    city: str
    state: str
    gender: int
    bday_day: int
    bday_month: int
    bday_year: int
    hobbies: list[int]
    pic: str