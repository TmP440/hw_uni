from typing import List, Callable

__all__ = ["get_squares_less_than_n"]


def check_n_between_0_and_20(func) -> Callable[[int], str | List[int]]:
    def wrapper(n: int):
        if 1 <= n <= 20:
            return func(n)
        else:
            return "The value of n should be in the range [1, 20]."

    return wrapper


@check_n_between_0_and_20
def get_squares_less_than_n(n: int) -> List[int]:
    return [i * i for i in range(n)]
