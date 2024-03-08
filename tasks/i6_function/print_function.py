__all__ = ["generate_1_n_string"]


def generate_1_n_string(n: int) -> str:
    return "".join([str(i) for i in range(1, n + 1)])
