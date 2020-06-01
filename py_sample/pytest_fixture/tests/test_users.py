from pytest_fixture import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_function_one(db):
    assert db.get(1).name == 'bob'


class TestUsers:
    def test_method_one(self, db):
        assert db.get(1).age == 10
