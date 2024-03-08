from typing import List

__all__ = ["count_man_in_T"]


def count_man_in_T(passenger_data: List[List[int]], moment: int) -> int:
    number_of_people_at_moment_T = len(
        [elem for elem in passenger_data if elem[0] <= moment <= elem[1]]
    )
    return number_of_people_at_moment_T
