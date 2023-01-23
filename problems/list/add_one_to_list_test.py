import add_one_to_list


def test_add():
    assert add_one_to_list.add_one_to_list([1]) == 2
    assert add_one_to_list.add_one_to_list([2, 3]) == 24
    assert add_one_to_list.add_one_to_list([8, 9]) == 90
    assert add_one_to_list.add_one_to_list([9, 9]) == 100
    assert add_one_to_list.add_one_to_list([0, 9, 9, 9]) == 1000
    assert add_one_to_list.add_one_to_list([0, 0, 9, 9, 9]) == 1000
