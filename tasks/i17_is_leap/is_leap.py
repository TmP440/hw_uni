__all__ = ["is_leap"]


def is_leap(year: int) -> bool:
    if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
        return True
    return False
