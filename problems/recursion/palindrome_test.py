import palindrome


def test_is_palindrome():
    assert palindrome.is_palindrome("a")
    assert palindrome.is_palindrome("abba")
    assert palindrome.is_palindrome("abcba")
    assert not palindrome.is_palindrome("")
    assert not palindrome.is_palindrome("abca")


def test_find_all_palindromes():
    assert palindrome.find_all_palindromes("a") == ["a"]
    assert palindrome.find_all_palindromes("ab") == []
    assert palindrome.find_all_palindromes("") == []
    assert palindrome.find_all_palindromes("abcba") == ["bcb", "abcba"]
