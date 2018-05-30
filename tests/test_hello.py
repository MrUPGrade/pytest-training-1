from app.funcs import msg_welcome, printer, print_welcome
from unittest.mock import Mock


def test_printer():
    result = msg_welcome('test')

    assert result == "Hi test!"


def test_printer2():
    m = Mock()

    print_welcome('haha', my_print=m)

    m.assert_called_with('Hi haha!')
