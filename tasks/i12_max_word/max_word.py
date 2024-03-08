import re

__all__ = ["read_file_and_find_max_length_word"]


def read_file_and_find_max_length_word(filename) -> list[str]:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        words = re.findall(r"\b\w+\b", content)

        if not words:
            print("Файл не содержит слов.")
            return []

        max_length = max(len(word) for word in words)
        max_length_words = [word for word in words if len(word) == max_length]

        for word in max_length_words:
            print(word)

    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
