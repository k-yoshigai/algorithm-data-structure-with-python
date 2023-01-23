from typing import List


def snake_string(chars: str, depth: int) -> List[List[str]]:
    result = [[] for _ in range(depth)]
    result_indexes = {i for i in range(depth)}
    insert_index = int(depth / 2)

    def up(x: int) -> int:
        return x + 1

    def down(x: int) -> int:
        return x - 1

    op = down

    for c in chars:
        result[insert_index].append(c)

        # Fills the rest elements of the list with empty strings.
        for rest_index in result_indexes - {insert_index}:
            result[rest_index].append(" ")

        if insert_index <= 0:
            op = up
        if insert_index >= depth - 1:
            op = down
        insert_index = op(insert_index)
    return result


if __name__ == "__main__":
    import string

    alphabet = [s for _ in range(2) for s in string.ascii_lowercase]
    print("".join(alphabet))
    print("-------------------------")

    for line in snake_string("".join(alphabet), 10):
        print("".join(line))
