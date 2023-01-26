from typing import List


def is_palindrome(s: str) -> bool:
    len_str = len(s)
    if not len_str:
        return False
    if len_str == 1:
        return True

    start, end = 0, len_str - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


def find_palindromes(s: str, left: int, right: int) -> List[str]:
    result = []
    while 0 <= left and right <= len(s) - 1:
        if s[left] != s[right]:
            break

        result.append(s[left : right + 1])
        left -= 1
        right += 1
    return result


def find_all_palindromes(s: str) -> List[str]:
    result = []
    len_str = len(s)

    if not len_str:
        return result

    if len_str == 1:
        result.append(s)
        return result

    for i in range(1, len_str):
        [result.append(x) for x in find_palindromes(s, i - 1, i + 1)]
        [result.append(x) for x in find_palindromes(s, i - 1, i)]

    return result
