__all__ = ["swap_case"]


def swap_case(input_string: str) -> str:
    swapped_string = ""
    for char in input_string:
        if char.islower():
            swapped_string += char.upper()
        elif char.isupper():
            swapped_string += char.lower()
        else:
            swapped_string += char
    return swapped_string


print(swap_case("Hello World!"))
