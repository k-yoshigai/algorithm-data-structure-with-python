import merge_sort


def test_selection_sort():
    in_ = [2, 11, 5, 2, 7, 13, 10]
    want = [2, 2, 5, 7, 10, 11, 13]
    assert want == merge_sort.merge_sort(in_)
