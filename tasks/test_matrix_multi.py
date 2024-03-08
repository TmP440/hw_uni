from tasks.i20_matrix.matrix_multi import *


def test_matrix_multi() -> None:
	n = 3
	matrix_1 = [
		[5, 7, 9],
		[3, 6, 5],
		[8, 9, 4]
		]
	matrix_2 = [
		[8, 9, 6],
		[4, 9, 0],
		[4, 2, 4]
		]
	result_matrix = [
		[104, 126, 66],
		[68, 91, 38],
		[116, 161, 64]
	]

	func_result = matrix_multi(matrix_1, matrix_2, n)
	assert func_result == result_matrix
