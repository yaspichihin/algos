import random


def quick_sort(arr, start, stop) -> None:
    """Быстрая сортировка, меняет список на месте."""

    if start > stop:
        return

    anchor = arr[start]
    left = start
    right = stop

    while left != right:

        # Движение справа налево, ищем число мееньше опорного
        while arr[right] >= anchor and left < right:
            right -= 1

        # Движение слево направо, ищем число больше опорного
        while arr[left] <= anchor and left < right:
            left += 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

    arr[start], arr[left] = arr[left], arr[start]
    quick_sort(arr, start, left - 1)
    quick_sort(arr, right + 1, stop)


if __name__ == "__main__":
    digits = [random.randint(0, 9) for _ in range(10)]
    print(digits)
    quick_sort(digits, 0, len(digits) - 1)
    print(digits)
