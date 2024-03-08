
__all__ = ["knapsack"]


def knapsack(cap: int, values: list[int], weights: list[int]) -> list[float]:
    items = []
    for i in range(len(values)):
        itemInfo = {
            'vpw': values[i] / weights[i],
            'weight': weights[i]
        }
        if len(items) == 0:
            items.append(itemInfo)
        else:
            k = 0
            while k < len(items) and items[k]['vpw'] > itemInfo['vpw']:
                k += 1
            items.insert(k, itemInfo)
    total = []
    cap_left = cap
    for item in items:
        if cap_left - item['weight'] >= 0:
            total.append(item['weight'] * item['vpw'])
            cap_left -= item['weight']
        elif cap_left > 0:
            total.append(item['vpw'] * cap_left)
            cap_left = 0
    return total
