from pytest import raises
from tasks.i9_list_functions.list_functions import *


def test_print(list_functions: MyList) -> None:
    result = list_functions.do_function("print")
    assert result == []


def test_append_one_elem_in_list(list_functions: MyList) -> None:
    list_functions.do_function("append", 1)
    result = list_functions.do_function("print")
    assert result == [1]


def test_append_two_elems_in_list(list_functions: MyList) -> None:
    list_functions.do_function("append", 1)
    list_functions.do_function("append", 5)
    result = list_functions.do_function("print")
    assert result == [1, 5]


def test_insert_one_elem_in_list(list_functions: MyList) -> None:
    list_functions.do_function("insert", 0, 1)
    result = list_functions.do_function("print")
    assert result == [1]


def test_insert_two_elems_in_list(list_functions: MyList) -> None:
    list_functions.do_function("insert", 0, 1)
    list_functions.do_function("insert", 0, 5)
    result = list_functions.do_function("print")
    assert result == [5, 1]


def test_remove_one_elem_from_list(list_functions: MyList) -> None:
    list_functions.do_function("append", 1)
    list_functions.do_function("append", 5)
    list_functions.do_function("remove", 1)
    result = list_functions.do_function("print")
    assert result == [5]


def test_remove_no_elem_from_list(list_functions: MyList) -> None:
    list_functions.do_function("append", 1)
    list_functions.do_function("append", 5)
    with raises(ValueError):
        list_functions.do_function("remove", 2)
    result = list_functions.do_function("print")
    assert result == [1, 5]


def test_sort_list(list_functions: MyList) -> None:
    for elem in [3, 2, 1]:
        list_functions.do_function("append", elem)
    list_functions.do_function("sort")
    result = list_functions.do_function("print")
    assert result == [1, 2, 3]


def test_reverse_list(list_functions: MyList) -> None:
    for elem in [1, 2, 3]:
        list_functions.do_function("append", elem)
    list_functions.do_function("reverse")
    result = list_functions.do_function("print")
    assert result == [3, 2, 1]


def test_pop_from_list(list_functions: MyList) -> None:
    list_functions.do_function("append", 1)
    list_functions.do_function("append", 2)
    list_functions.do_function("pop")
    result = list_functions.do_function("print")
    assert result == [1]
