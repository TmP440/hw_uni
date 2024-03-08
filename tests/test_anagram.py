from tasks.i14_anagram.anagram import *
from pytest import mark


@mark.parametrize(
    "word_1, word_2, result",
    [
        (
            "zxcqwe",
            "wcxzeq",
            True,
        ),
        (
            "zxcqwe",
            "qwezxc",
            True,
        ),
        (
            "asd",
            "aasd",
            False,
        ),
        (
            "qaz",
            "wsx",
            False,
        ),
        (
            "",
            "",
            True,
        ),
    ],
)
def test_anagram(word_1, word_2, result) -> None:
    func_result = is_anagram(word_1, word_2)
    assert func_result == result
