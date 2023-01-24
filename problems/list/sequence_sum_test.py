import sequence_sum


def test_get_sequence_sum():
    assert sequence_sum.get_max_sequence_sum([1, 2, 3]) == 6
    assert sequence_sum.get_max_sequence_sum([]) == 0
    assert sequence_sum.get_max_sequence_sum([1, 2, 3, -4]) == 6


def test_get_max_circular_sequence_sum():
    assert sequence_sum.get_max_circular_sequence_sum([1, 2, 3]) == 6
    assert sequence_sum.get_max_circular_sequence_sum([]) == 0
    assert sequence_sum.get_max_circular_sequence_sum([1, 2, 3, -4]) == 6
    assert sequence_sum.get_max_circular_sequence_sum([3, -1, 2, -3, 1]) == 4
