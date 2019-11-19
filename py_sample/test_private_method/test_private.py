import pytest

from sample import Sample


class TestClass:
    def test_public_method(self):
        s = Sample()
        assert s.public_method() == 'public_method'

    def test_private_method_u(self):
        s = Sample()
        assert s._private_method_u() == '_private_method_u'

    def test_private_method_uu(self):
        s = Sample()
        assert s.__private_method_uu() == '__private_method_uu'

    def test_private_method_uu_mang(self):
        s = Sample()
        assert s._Sample__private_method_uu() == '__private_method_uu'
