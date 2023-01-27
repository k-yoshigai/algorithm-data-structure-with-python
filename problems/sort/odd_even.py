from typing import List


def even_first_odd_last(numbers: List[int]) -> None:
    i, j = 0, len(numbers) - 1

    while i < j:
        if numbers[i] % 2 == 0:
            i += 1
        else:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j -= 1
