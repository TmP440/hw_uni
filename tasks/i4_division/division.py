from typing import Tuple

__all__ = ["division"]


def division(a: int, b: int) -> Tuple[int | str, float | str]:
    if b != 0:
        _mod: int = a // b
        _div: float = a / b
        return _mod, _div
    else:
        return "ZeroDivisionError", "ZeroDivisionError"
