from unittest.mock import Mock
import pytest


@pytest.fixture(scope='session')
def dummy_db(request):
    a = Mock()
    a.get_users.return_value = ['Kasia', 'Tomek']

    def func():
        print('koniec')

    request.addfinalizer(func)

    return a
