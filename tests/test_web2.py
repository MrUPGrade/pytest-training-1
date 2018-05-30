import pytest

from app.web import BusinessLogic


class TestBusinessLogic:
    def test_1(self, dummy_db):
        b = BusinessLogic(dummy_db)

        result = b.get_user_ended_with('k')

        assert result == ['Tomek']
