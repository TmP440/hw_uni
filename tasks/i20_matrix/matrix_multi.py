
__all__ = ["matrix_multi"]


def matrix_multi(matrix_1: list[list[int]], matrix_2: list[list[int]], n: int) -> list[list[int]]:
	result_matrix = [[0 for i in range(n)] for i in range(n)]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				result_matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]
	return result_matrix
