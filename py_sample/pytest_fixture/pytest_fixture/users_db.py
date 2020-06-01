from .user import User


class Users:
    def __init__(self):
        self._last_insert_id = 0
        self._rows = dict()

    def insert(self, name: str, age: int):
        self._last_insert_id += 1
        user = User(
            user_id=self._last_insert_id,
            name=name,
            age=age
        )
        self._rows[self._last_insert_id] = user

    def get(self, user_id: int) -> User:
        return self._rows.get(user_id)
