__all__ = ["is_anagram"]


def is_anagram(word_1: str, word_2: str) -> bool:
    if len(word_1) != len(word_2):
        return False

    sorted_word_1_by_letter = sorted(list(word_1.lower()))
    sorted_word_2_by_letter = sorted(list(word_2.lower()))

    if sorted_word_1_by_letter == sorted_word_2_by_letter:
        return True
    return False
