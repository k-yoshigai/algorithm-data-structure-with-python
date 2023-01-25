import permutation


def test_all_perms():
    expected_lists = [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]
    for result, expected in zip(permutation.all_perms([1, 2, 3]), expected_lists):
        assert result == expected
