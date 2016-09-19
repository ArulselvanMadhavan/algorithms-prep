"""Pure Python."""
import unittest


def is_pangram(input_str):
    """Check if pangram."""
    input_str = input_str.lower()
    arr = [0] * 26
    lower_case_a = ord("a")
    for char in input_str:
        cur_value = ord(char) - lower_case_a
        if cur_value >= 0 and cur_value <= 25:
            arr[cur_value] = 1
    for i in range(26):
        if arr[i] != 1:
            return "not pangram"
    return "pangram"

if __name__ == '__main__':
    input_str = input().strip()
    print(is_pangram(input_str))


class TestPangram(unittest.TestCase):
    """Pangram Tests."""

    def test_basic(self):
        """Basic tests."""
        self.assertEqual(is_pangram("We promptly judged antique ivory buckles \
        for the next prize"), "pangram")
        self.assertEqual(is_pangram("We promptly judged antique ivory buckles \
        for the prize "), "not pangram")
