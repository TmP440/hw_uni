import pytest
from tasks.i3_arith_oper.arithmetic_operators import *


@pytest.mark.parametrize(
    "number1, number2, returned_results",
    (
        [
            1,
            2,
            [3, -1, 2],
        ],
        [
            0,
            0,
            [0, 0, 0],
        ],
        [
            -2,
            3,
            [1, -5, -6],
        ],
        [
            2,
            -3,
            [-1, 5, -6],
        ],
        [
            -2,
            -3,
            [-5, 1, 6],
        ],
        [
            4,
            0,
            [4, 4, 0],
        ],
        [0, 4, [4, -4, 0]],
    ),
)
def test_arithmetic_operators(number1, number2, returned_results):
    func_result = addition_subtraction_multiplication(number1, number2)
    assert func_result == returned_results
