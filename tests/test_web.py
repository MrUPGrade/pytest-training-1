from unittest.mock import Mock

from app.web import BusinessLogic, DB
import pytest


class Dummy():
    def get_users(self):
        return ['Kasia', 'Tomek']


def test_business_logic_get_users():
    a = Dummy()
    b = BusinessLogic(a)

    result = b.get_user_ended_with('k')

    assert result == ['Tomek']


def test_business_logic_get_users2(dummy_db):
    b = BusinessLogic(dummy_db)

    result = b.get_user_ended_with('k')

    assert result == ['Tomek']


def test_business_logic_get_users3(dummy_db):
    b = BusinessLogic(dummy_db)

    with pytest.raises(ValueError):
        b.get_user_ended_with(1)


@pytest.mark.parametrize('letter,expected',
                         [
                             ('k', ['Tomek']),
                             ('a', ['Kasia'])
                         ]
                         )
def test_business_logic_get_users_params(letter, expected, dummy_db):
    b = BusinessLogic(dummy_db)

    result = b.get_user_ended_with(letter)

    assert result == expected
