import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, output_str", [
    ("hello", "Hello"),
    ("hello world", "Hello world"),
    ("февраль 2025", "Февраль 2025")
])
def test_capitalize_positive(input_str, output_str):
    assert string_utils.capitalize(input_str) == output_str

@pytest.mark.negative
@pytest.mark.parametrize("input_str, output_str",[
    (" ", " "),
    ("123", "123"),
    ("", "")
])
def test_capitalize_negative(input_str, output_str):
    assert string_utils.capitalize(input_str) == output_str

#Удаление пробелов
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  hello", "hello"),
    (" Hi", "Hi")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.xfail
@pytest.mark.parametrize("input_str, expected", [
    ("  winter", "  winter"),
    (" sun", " sun")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

#Искомый символ
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, result", [
    ("word", "o", True),
    ("5,6,7", "6", True),
    ("hello", "y", False)
])
def test_contains_positive(string, symbol, result):
    res = string_utils.contains(string, symbol)
    assert res == result

@pytest.mark.negative
@pytest.mark.xfail
@pytest.mark.parametrize("string, symbol, result", [
    ("word", "o", False),
    ("5,6,7", "9", True),
    ("hello", "y", True)
])
def test_contains_negative(string, symbol, result):
    res = string_utils.contains(string, symbol)
    assert res == result

#Удаление символа
@pytest.mark.positive
@pytest.mark.parametrize("val, sym, result", [
    ("winter", "n", "witer"),
    ("catdog", "dog", "cat")
])
def test_delete_positive(val, sym, result):
    res = string_utils.delete_symbol(val, sym)
    assert res == result

@pytest.mark.negative
@pytest.mark.xfail
@pytest.mark.parametrize("val, sym, result", [
        ("winter", "n", "winter"),
        ("summer", "m", "summer")
    ])
def test_delete_negative(val, sym, result):
        res = string_utils.delete_symbol(val, sym)
        assert res == result
