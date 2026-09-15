def count_words(text: str) -> int:
    """Count the number of words in a string, splitting on whitespace."""
    return len(text.split())


def is_palindrome(text: str) -> bool:
    """Check whether text is a palindrome, ignoring case and spaces."""
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]
