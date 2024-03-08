from tasks.i15_metro.metro import *
from pytest import mark


@mark.parametrize(
    "passenger_data, moment, result",
    [
        (
            [
                [9, 12],
            ],
            12,
            1,
        ),
        (
            [
                [12, 14],
            ],
            12,
            1,
        ),
        (
            [
                [10, 15],
            ],
            12,
            1,
        ),
        (
            [
                [1, 8],
            ],
            12,
            0,
        ),
        (
            [
                [13, 15],
            ],
            12,
            0,
        ),
    ],
)
def test_metro(passenger_data, moment, result):
    func_result = count_man_in_T(passenger_data, moment)
    assert func_result == result
