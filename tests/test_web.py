from unittest.mock import Mock

from app.web import BusinessLogic, DB


class Dummy():
    def get_users(self):
        return ['Kasia', 'Tomek']


def test_business_logic_get_users():
    a = Dummy()
    b = BusinessLogic(a)

    result = b.get_user_ended_with('k')

    assert result == ['Tomek']


def test_business_logic_get_users2():
    a = Mock()
    b = BusinessLogic(a)

    a.get_users.return_value = ['Kasia', 'Tomek']

    result = b.get_user_ended_with('k')

    assert result == ['Tomek']
