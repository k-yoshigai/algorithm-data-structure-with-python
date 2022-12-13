from typing import List


def linear_search(numbers: List[int], value: int) -> int:
    for i in range(0, len(numbers)):
        if numbers[i] == value:
            return i
    return -1


# partern 1
def binary_search1(numbers: List[int], value: int) -> int:
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# partern 2
def binary_search2(numbers: List[int], value: int) -> int:
    def _binary_search(numbers: List[int], value: int, left: int, right: int) -> int:
        if left > right:
            return -1
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            return _binary_search(numbers, value, mid + 1, right)
        else:
            return _binary_search(numbers, value, left, mid - 1)

    return _binary_search(numbers, value, 0, len(numbers) - 1)


if __name__ == "__main__":
    nums = [3, 48, 2, 10, 43, 28]
    nums = sorted(nums)
    test_cases = [
        {"want": 0, "value": 2},
        {"want": 5, "value": 48},
        {"want": 2, "value": 10},
        {"want": -1, "value": 11},
    ]

    for test_case in test_cases:
        result1 = binary_search1(nums, test_case["value"])
        result2 = binary_search2(nums, test_case["value"])
        assert result1 == result2 == test_case["want"]
