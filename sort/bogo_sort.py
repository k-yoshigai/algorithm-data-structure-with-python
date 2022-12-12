import random
from typing import List


def in_order(numbers: List[int]) -> bool:
    return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))


def bogo_sort(numbers: List[int]) -> List[int]:
    while not in_order(numbers):
        random.shuffle(numbers)
    return numbers


if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(f"nums(before sorting): {nums}")
    print(f"nums(after sorting) : {bogo_sort(nums)}")
