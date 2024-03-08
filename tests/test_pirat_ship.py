from tasks.i19_pirat_ship.pirat_ship import *


def test_pirat_ship() -> None:
	cap = 60
	values = [60, 100, 120]
	weight = [20, 50, 30]
	func_result = knapsack(cap, values, weight)
	assert func_result == [120.0, 60.0, 20.0]
