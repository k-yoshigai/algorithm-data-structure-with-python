from typing import List


def add_one_to_list(nums: List[int]) -> int:
    reversed_nums = []
    carry_up_flg = False

    for i, num in enumerate(reversed(nums)):
        if carry_up_flg or i == 0:
            num += 1

        if num >= 10:
            carry_up_flg = True
            num = 0
        else:
            carry_up_flg = False

        reversed_nums.append(num)

        if i == len(nums) - 1 and carry_up_flg:
            reversed_nums.append(1)

    total = 0
    for i, num in enumerate(reversed_nums):
        total += num * 10**i
    return total
