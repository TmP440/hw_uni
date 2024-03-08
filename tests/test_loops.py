import pytest
from tasks.i5_loops.loops import *


@pytest.mark.parametrize(
    "n, result",
    [(i, [x * x for x in range(i)]) for i in range(1, 21)],
)
def test_loop_OK(n, result):
    func_result = get_squares_less_than_n(n)
    assert func_result == result


def test_loop_error():
    func_result = get_squares_less_than_n(21)
    assert func_result == "The value of n should be in the range [1, 20]."
