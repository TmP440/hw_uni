import pytest
from tasks.i4_division.division import *


@pytest.mark.parametrize(
    "num1, num2, result",
    [
        (
            1,
            2,
            (0, 0.5),
        ),
        (
            2,
            1,
            (2, 2.0),
        ),
        (5, 0, ("ZeroDivisionError", "ZeroDivisionError")),
        (0, 5, (0, 0.0)),
    ],
)
def test_division(num1, num2, result):
    func_result = division(num1, num2)
    assert func_result == result
