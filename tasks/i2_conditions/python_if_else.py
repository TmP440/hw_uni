__all__ = ["check_number"]


def check_number(num: int) -> str:
    if num % 2 == 0:
        if 2 <= num <= 5:
            return "Not Weird"
        elif 6 <= num <= 20:
            return "Weird"
        elif num > 20:
            return "Not Weird"
    else:
        return "Weird"
