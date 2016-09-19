"""Pure Python."""
import unittest


def min_cost(input_str):
    """Input String."""
    const_str = [0] * 26
    lower_case_a = ord("a")
    cost = 0
    for i in input_str:
        char_val = ord(i) - lower_case_a
        if const_str[char_val] != 1:
            cost += 1
            const_str[char_val] = 1
    return cost


if __name__ == '__main__':
    n = int(input().strip())
    for a0 in range(n):
        s = input().strip()
        print(min_cost(s))


class TestMinCost(unittest.TestCase):
    """Test Class."""

    def test_basic(self):
        """Basic."""
        self.assertEqual(min_cost("abcd"), 4)
        self.assertEqual(min_cost("abab"), 2)
