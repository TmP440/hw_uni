from pytest import mark
from tasks.i10_swap_case.swap_case import *


@mark.parametrize(
    "input_string, result",
    [
        (
            "Hello World!",
            "hELLO wORLD!",
        ),
        (
            "Www.MosPolytech.ru",
            "wWW.mOSpOLYTECH.RU",
        ),
        (
            "Pythonist 2",
            "pYTHONIST 2",
        ),
        (
            "Привет Мир!",
            "пРИВЕТ мИР!",
        ),
        (
            "1234567890!@#$%^&*()_+?></.," "}]{[|\?`:;",
            "1234567890!@#$%^&*()_+?></.," "}]{[|\?`:;",
        ),
    ],
)
def test_swap_case(input_string, result) -> None:
    func_result = swap_case(input_string)
    assert func_result == result
