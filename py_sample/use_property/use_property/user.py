from dataclasses import dataclass
from datetime import date

@dataclass
class User:
    username: str
    birthday: date

    @property
    def age(self):
        today = date.today()
        age = int((today - self.birthday).days / 365.25)
        if (self.birthday.month, self.birthday.day) < (today.month, today.day):
            age -= 1
        return age
    
    def age_display(self) -> str:
        return f"{self.age} year old."
