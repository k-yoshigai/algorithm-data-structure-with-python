from typing import List


def sort_alphabets_by_indexes(chars: List[str], indexes: List[int]) -> str:
    i = 0
    while i < len(indexes) - 1:
        while i != indexes[i]:
            index = indexes[i]
            chars[i], chars[index] = chars[index], chars[i]
            indexes[i], indexes[index] = indexes[index], indexes[i]
        i += 1
    return "".join(chars)
