from app.funcs import print_welcome
from unittest.mock import Mock

def test_printer():
    result = print_welcome('test')

    assert result == "Hi test!"
