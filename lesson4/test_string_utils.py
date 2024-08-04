import pytest
from string_utils import StringUtils
utils = StringUtils()

#"""Capitalize"""

#def test_capitalize():
#  """Positive"""
#    assert utils.capitalize("asus") == "Asus"
#    assert utils.capitalize("my name is..") == "My name is.."
#    assert utils.capitalize("1234") == "1234"
#
#   """Negative"""
#    assert utils.capitalize("") == ""
#    assert utils.capitalize(" ") == " "
#    assert utils.capitalize("test1234") == "test1234" 

"""trim"""

@pytest.mark.parametrize("input_string, expected_output", [
    (" asus", "asus"),
    (" asus ", "asus "),
])
def test_string(input_string, expected_output):
    assert utils.trim(input_string) == expected_output

#NEGATIVE

def test_trim():
    assert utils.trim("") == ""

@pytest.mark.xfail()
def test_trim_number():
   assert utils.trim(12345) == "12345"

@pytest.mark.xfail()
def test_trim_with_probel():
   assert utils.trim(" rain ") == " rain "


"""to_list"""

@pytest.mark.parametrize("string, delimetr, result", [
    ("1,2,3,4,5", ",", ["1", "2", "3", "4", "5"]),
    ("весна/осень", "/", ["весна", "осень"]),
    #negative
    ("", None, [])
])
def test_to_list(string, delimetr, result):
    if delimetr is None:
       res = utils.to_list(string)
    else:
       res = utils.to_list(string, delimetr)
    assert res == result


"""contains"""
 
@pytest.mark.parametrize("string, symbol, result", [
   ("Нежность", "ж", True),
   ("123", "2", True),
   ("", "", True),
   ("Ижевск", "И", True),
   ("Город-герой", "-", True),
   ("123", "f", False),
   ("Ижевск", "и", False),
   ("", "2", False),
   #("привет", "", False)
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result



"""delete_symbol"""

@pytest.mark.parametrize("string, symbol, result", [
   ("Summer", "m", "Suer"),
   ("123", "3", "12"),
   ("диван-кровать", "-", "диванкровать"),
   ("cat dog", " ", "catdog"),
   ("морковь ", " ", "морковь"),
   ("", "", "")
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result


"""start_with"""

@pytest.mark.parametrize("string, symbol, result", [
    ("Summer", "S", True),
    (" apple", " ", True),
    ("123", "1", True),
    ("apple", "A", False),
    ("Мир", "м", False),
    ("", "d", False),
    ("мир", "ж", False)
])
def test_start_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result

"""end_with"""

@pytest.mark.parametrize("string, symbol, result", [
    ("Summer", "r", True),
    (" apple", "e", True),
    ("123", "3", True),
    ("apple ", " ", True),
    ("Мир", "м", False),
    ("", "d", False),
    ("мир", "ж", False)
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result

"""is_empty"""

@pytest.mark.parametrize("string, result", [
    ("", True),
    (" ", True),
    ("A", False),
    (" A", False),
    ("12", False)
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result

"""list_to_string"""

@pytest.mark.parametrize("lst, joiner, result", [
    ([1, 2, 2, 3, 5], None, "1, 2, 2, 3, 5"),
    (["диван", "кровать"], "-", "диван-кровать"),
    (["s", "o", "s"], "", "sos"),

    ([], "", ""),
    ([], None, ""),
    ([], "a", "")
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
       res = utils.list_to_string(lst)
    else:
       res = utils.list_to_string(lst, joiner)
    assert res == result

