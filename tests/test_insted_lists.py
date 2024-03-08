from pytest import mark
from tasks.i8_insted_lists.insted_lists import *


@mark.parametrize(
    "student_data, second_score_students",
    [
        ([["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]], ["alpha", "beta"]),
        (
            [
                [
                    "Гарри",
                    37.21,
                ],
                [
                    "Берри",
                    37.21,
                ],
                [
                    "Тина",
                    37.2,
                ],
                [
                    "Акрити",
                    41,
                ],
                [
                    "Харш",
                    39,
                ],
            ],
            ["Берри", "Гарри"],
        ),
        (
            [
                [
                    "Zero_1",
                    0.0,
                ],
                [
                    "Zero_2",
                    0.0,
                ],
                [
                    "Zero_3",
                    0.0,
                ],
            ],
            [],
        ),
    ],
)
def test_student_in_second_place(student_data, second_score_students):
    func_result = student_in_second_place(student_data)
    assert func_result == second_score_students
