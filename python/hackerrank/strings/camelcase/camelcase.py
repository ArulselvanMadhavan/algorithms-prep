"""Pure Python."""
import unittest


def get_words(input_str):
    """Split camelCase to words."""
    input_chars = list(input_str)
    input_len = len(input_str)
    words_count = 1
    for i in range(input_len):
        if input_chars[i].isupper():
            words_count += 1
    return words_count


if __name__ == '__main__':
    input_str = input().strip()
    print(get_words(input_str))


class TestGetWords(unittest.TestCase):
    """Test class."""

    def test_basic(self):
        """Basic tests."""
        self.assertEqual(get_words("saveChangesInTheEditor"), 5)
