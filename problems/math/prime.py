import math
from typing import List


def generate_primes(num: int) -> List[int]:
    result = []
    cache = {}

    for i in range(2, num + 1):
        is_prime = cache.get(i)

        if is_prime is False:
            continue

        result.append(i)
        cache[i] = True

        for j in range(i * 2, num + 1, i):
            cache[j] = False
    return result


def is_prime(num: int) -> bool:
    if num <= 1:
        return False

    for i in range(2, math.ceil(num)):
        if num % i == 0:
            return False
    return True
