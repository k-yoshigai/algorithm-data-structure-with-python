import crypto


def test_caesar_cipher():
    assert crypto.caesar_cipher("abc", 2) == "cde"
    assert crypto.caesar_cipher("xyz", 2) == "zab"
    assert crypto.caesar_cipher("abc", 0) == "abc"

    assert crypto.caesar_cipher("cde", -2) == "abc"
    assert crypto.caesar_cipher("zab", -2) == "xyz"
