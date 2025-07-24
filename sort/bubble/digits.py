import random


def bubble_sort(digits: list[int]) -> None:
    """Мутирует переданный параметр"""

    for i in range(len(digits), 0, -1):
        for j in range(i - 1):
            if digits[j] > digits[j + 1]:
                digits[j], digits[j + 1] = digits[j + 1], digits[j]


if __name__ == "__main__":
    digits = [random.randint(0, 1_000) for _ in range(100)]
    bubble_sort(digits)
    assert digits == sorted(digits), "Ошибка сортировки"
