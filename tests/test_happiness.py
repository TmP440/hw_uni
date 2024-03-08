from tasks.i18_happiness.happiness import *


def test_happiness():
    list_number = [1, 5, 3]
    good_set = {3, 1}
    bad_set = {5, 7}

    func_result = am_i_happy(list_number, good_set, bad_set)
    assert func_result == 1
