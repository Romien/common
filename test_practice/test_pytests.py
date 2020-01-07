import pytest

from tasks import (
    convert_num,
    largest_word,
    backwards,
    even_numbers,
    add_to_input,
    factorial,
    change_letter,
    alphabet_order,
    compare_numbers
)


@pytest.mark.parametrize(
    "a, expected",
    [
        (63, '1:3'),
        (185, '3:5'),
        (6, '0:6'),
    ],
)
def test_convert_num(a, expected):
    assert convert_num(a) == expected


@pytest.mark.parametrize(
    "a, expected",
    [
        ("fun&!! time", "time"),
        ("full&!! time", "full"),
        ("fu-ll^& working day", "working"),
    ],
)
def test_largest_word(a, expected):
    assert largest_word(a) == expected


def test_backwards():
    s = "My name is Michele"
    result = backwards(s)
    assert result == "Michele is name My"


def test_even_numbers():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    result = even_numbers(a)
    expected = [4, 16, 36, 64, 100]
    assert result == expected


def test_add_to_input():
    result = add_to_input(4)
    assert result == 10


def test_factorial():
    result = factorial(4)
    assert result == 24


def test_change_letter():
    result = change_letter('abcd')
    assert result == 'bcdE'


def test_alphabet_order():
    result = alphabet_order('hello')
    assert result == 'ehllo'


def test_compare_numbers():
    result = compare_numbers(2, 5)
    assert result == True
