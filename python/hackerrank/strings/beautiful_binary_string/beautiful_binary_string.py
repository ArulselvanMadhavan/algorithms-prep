"""Pure Python."""
import unittest


def get_min_beautify(input_str):
    """Get min count to beautify the string."""
    prev = 0
    cur = 1
    next_ptr = 2
    input_len = len(input_str)
    input_str = list(input_str)
    count = 0
    while next_ptr < input_len:
        if input_str[prev] == "0" and input_str[cur] == "1" and input_str[next_ptr] == "0":
            prev += 3
            cur += 3
            next_ptr += 3
            count += 1
        else:
            prev += 1
            cur += 1
            next_ptr += 1
    return count

if __name__ == '__main__':
    n = int(input().strip())
    B = input().strip()
    print(get_min_beautify(n, B))


class TestBeautifulBinaryString(unittest.TestCase):
    """Beautiful String."""

    def test_basic(self):
        """Basic."""
        self.assertEqual(get_min_beautify("0101010"), 2)
        self.assertEqual(get_min_beautify("01100"), 0)
        self.assertEqual(get_min_beautify("0100101010"), 3)
