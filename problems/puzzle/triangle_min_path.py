import random
from typing import List, Optional


def generate_triangle_list(depth: int, max_num: int) -> List[List[int]]:
    return [[random.randint(0, max_num) for _ in range(i + 1)] for i in range(depth)]


def pirnt_triangle(data: List[List[int]]) -> None:
    max_digit = max([max(nums) for nums in data])
    width = max_digit + max_digit % 2 + 2
    for index, line in enumerate(data):
        numbers = "".join([str(n).center(width, " ") for n in line])
        print(" " * int(width / 2) * (len(data) - index), numbers)


def sum_min_path(triangle: List[List[int]]) -> Optional[int]:
    tree_sum = triangle[:]
    j, len_triangle = 1, len(triangle)

    if not len_triangle:
        return (None, [])

    while j < len_triangle:
        line = triangle[j]
        line_path_sum = []

        for i, value in enumerate(line):
            if i == 0:
                sum_value = line[i] + tree_sum[j - 1][0]
            elif i == len(line) - 1:
                sum_value = line[i] + tree_sum[j - 1][len(tree_sum[j - 1]) - 1]
            else:
                min_path = min(tree_sum[j - 1][i - 1], tree_sum[j - 1][i])
                sum_value = line[i] + min_path
            line_path_sum.append(sum_value)
        tree_sum[j] = line_path_sum
        j += 1
    return min(tree_sum[-1])


if __name__ == "__main__":
    triangle = generate_triangle_list(3, 6)
    pirnt_triangle(triangle)
    print(f"min path: {sum_min_path(triangle)}")
