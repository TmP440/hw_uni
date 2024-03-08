import pytest
from tasks.i6_function.print_function import *


@pytest.mark.parametrize(
    "n, output_str",
    [(i, "".join([str(j) for j in range(1, i + 1)])) for i in range(1, 20)],
)
def test_generate_1_n_string(n, output_str):
    func_result = generate_1_n_string(n)
    assert func_result == output_str
