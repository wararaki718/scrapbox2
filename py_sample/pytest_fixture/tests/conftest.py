import pytest

from pytest_fixture.users_db import Users


@pytest.fixture
def db():
    users = Users()
    users.insert('bob', 10)
    users.insert('alice', 20)
    return users
