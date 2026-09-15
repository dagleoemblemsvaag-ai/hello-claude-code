from text_utils import count_words, is_palindrome


def test_count_words_basic():
    assert count_words("hello world") == 2


def test_count_words_empty():
    assert count_words("") == 0


def test_is_palindrome_true():
    assert is_palindrome("A man a plan a canal Panama") is True


def test_is_palindrome_false():
    assert is_palindrome("hello") is False


def test_is_palindrome_empty_string():
    assert is_palindrome("") is True
