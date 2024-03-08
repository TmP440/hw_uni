from pytest import mark
from tasks.i11_split_and_join.split_and_join import *


@mark.parametrize(
    "input_string, result",
    [
        (
            "this is a string",
            "this-is-a-string",
        ),
        (
            "",
            "",
        ),
        (
            " ",
            "-",
        ),
    ],
)
def test_swap_case(input_string, result) -> None:
    func_result = split_and_join(input_string)
    assert func_result == result
