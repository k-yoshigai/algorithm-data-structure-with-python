import insertion_sort


def test_insertion_sort():
    in_ = [2, 11, 5, 2, 7, 13, 10]
    want = [2, 2, 5, 7, 10, 11, 13]
    assert want == insertion_sort.insertion_sort(in_)
