from typing import List

__all__ = ["second_score"]


def second_score(participants: List[int]) -> int | None:
    max_score = max(participants)
    filtered_scores = [score for score in participants if score != max_score]

    if not filtered_scores:
        return None

    second_max_score = max(filtered_scores)
    return second_max_score


print(second_score([2, 1, 2]))
