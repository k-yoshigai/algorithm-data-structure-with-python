from typing import List


def delete_duplicate(numbers: List[int]) -> None:
    tmp = []
    for num in numbers:
        if num not in tmp:
            tmp.append(num)
    numbers[:] = tmp


if __name__ == "__main__":
    l = [1, 2, 2, 3, 4, 5]
    print(l)
    delete_duplicate(l)
    print(l)
