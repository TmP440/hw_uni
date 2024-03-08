from typing import List

__all__ = ["addition_subtraction_multiplication"]


def addition_subtraction_multiplication(a: int, b: int) -> List[int]:
    addition: int = a + b
    subtraction: int = a - b
    multiplication: int = a * b
    return [addition, subtraction, multiplication]
