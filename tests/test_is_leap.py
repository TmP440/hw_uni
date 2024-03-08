from pytest import mark
from tasks.i17_is_leap.is_leap import *


@mark.parametrize(
    "year, result",
    [
        (
            2004,
            True,
        ),
        (
            2000,
            True,
        ),
        (
            1212,
            True,
        ),
        (
            1214,
            False,
        ),
    ],
)
def test_is_leap(year, result):
    func_result = is_leap(year)
    assert func_result == result
