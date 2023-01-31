from typing import List, Tuple


def get_hanoi_movement(disk: int, src: str, dest: str, support: str) -> List[Tuple[int, str, str]]:
    result = []

    def _hanoi(disk: int, src: str, dest: str, support: str):
        if disk < 1:
            return

        _hanoi(disk - 1, src, support, dest)
        result.append((disk, src, dest))
        _hanoi(disk - 1, support, dest, src)

    _hanoi(disk, src, dest, support)
    return result


if __name__ == "__main__":
    for r in get_hanoi_movement(2, "A", "C", "B"):
        print(r)
