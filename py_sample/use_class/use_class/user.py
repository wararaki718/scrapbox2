from dataclasses import dataclass
from datetime import date


@dataclass
class User:
    lastname: str
    firstname: str
    birthday: date

    @property
    def fullname(self) -> str:
        return f'{self.firstname}.{self.lastname}'
    
    @property
    def age(self) -> int:
        today = date.today()
        born = self.birthday
        age = today.year - born.year
        if (today.month, today.day) < (born.month, born.day):
            return age - 1
        else:
            return age
