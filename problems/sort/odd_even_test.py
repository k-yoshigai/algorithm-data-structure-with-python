from typing import List

import odd_even


def verify_even_first_odd_last(numbers: List[int]) -> bool:
    odd_started = False
    for num in numbers:
        if num % 2 != 0:
            odd_started = True
        if odd_started and num % 2 == 0:
            return False
    return True


def test_even_first_odd_last():
    l = [1, 3, 0, 2]
    odd_even.even_first_odd_last(l)
    assert verify_even_first_odd_last(l)
