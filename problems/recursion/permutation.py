from typing import List


def all_perms(numbers: List[int]) -> List[List[int]]:
    if len(numbers) <= 1:
        yield numbers
    else:
        for perm in all_perms(numbers[1:]):
            for i in range(len(numbers)):
                yield perm[:i] + numbers[0:1] + perm[i:]
