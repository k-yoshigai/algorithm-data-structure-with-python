import sort_alphabet


def test_sort_alphabet():
    assert sort_alphabet.sort_alphabets_by_indexes(["h", "y", "n", "p", "t", "o"], [3, 1, 5, 0, 2, 4]) == "python"
