from typing import List, Callable

__all__ = ["student_in_second_place"]


def check_empty_second_score(
    func: Callable[[List[List[str | float]]], List[str]]
) -> Callable[[List[List[str | float]]], List[str]]:
    def wrapper(student_scores: List[List[str | float]]):
        try:
            tmp_check = sorted(set(student[1] for student in student_scores))[1]
            return func(student_scores)
        except IndexError:
            return []

    return wrapper


@check_empty_second_score
def student_in_second_place(student_scores: List[List[str | float]]) -> List[str]:
    second_place_score = sorted(set(student[1] for student in student_scores))[1]

    second_place_students = sorted(
        [student[0] for student in student_scores if student[1] == second_place_score]
    )
    return second_place_students
