from typing import List


def get_max_sequence_sum(numbers: List[int]) -> int:
    max_sequence_sum, tmp_sum = 0, 0
    for num in numbers:
        tmp_sum = max(num, tmp_sum + num)
        max_sequence_sum = max(max_sequence_sum, tmp_sum)
    return max_sequence_sum


def get_max_circular_sequence_sum(numbers: List[int]) -> int:
    return max(get_max_sequence_sum(numbers), sum(numbers) - get_max_sequence_sum(numbers))
