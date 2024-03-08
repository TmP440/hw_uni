import pytest
from tasks.i2_conditions.python_if_else import *


@pytest.mark.parametrize(
    "input_num, returned_value",
    (
        [
            0,
            None,
        ],
        [
            1,
            "Weird",
        ],
        [
            2,
            "Not Weird",
        ],
        [
            4,
            "Not Weird",
        ],
        [
            5,
            "Weird",
        ],
        [
            6,
            "Weird",
        ],
        [7, "Weird"],
        [
            20,
            "Weird",
        ],
        [21, "Weird"],
        [
            22,
            "Not Weird",
        ],
    ),
)
def test_check_number(input_num: int, returned_value: str):
    func_result = check_number(input_num)
    assert func_result == returned_value
