from pytest import mark
from tasks.i7_second_score.second_score import *


@mark.parametrize(
    "l, result",
    (
        [[0], None],
        [[0, 1], 0],
        [
            [2, 1, 3],
            2,
        ],
        [
            [1, 5, 12, 11, 3, 43],
            12,
        ],
        [
            [2, 1, 2],
            1,
        ],
        [[1, 1, 1], None],
    ),
)
def test_second_score(l, result):
    func_result = second_score(l)
    assert func_result == result
