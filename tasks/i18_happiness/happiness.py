__all__ = ["am_i_happy"]


def am_i_happy(list_numbers: list[int], good_set: set[int], bad_set: set[int]) -> int:

    my_happiness: int = 0

    for num in list_numbers:
        if num in good_set:
            my_happiness += 1
        elif num in bad_set:
            my_happiness -= 1

    return my_happiness
