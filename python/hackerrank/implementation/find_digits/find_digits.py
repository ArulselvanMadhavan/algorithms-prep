"""Pure Python."""
import unittest


def integer_to_array(num):
    """Int to array."""
    i = 0
    arr = [-1] * 10
    while num:
        arr[i] = num % 10
        num //= 10
        i += 1
    return arr


def evenly_divisible_digits(num):
    """Even Divisible digits."""
    arr = integer_to_array(num)
    even_digits = 0
    i = 0
    while arr[i] != -1:
        if arr[i] != 0 and num % arr[i] == 0:
            even_digits += 1
        i += 1
    return even_digits

if __name__ == '__main__':
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(evenly_divisible_digits(n))


class TestEvenlyDivisibleDigits(unittest.TestCase):
    """Test Case."""

    def test_basic(self):
        """Basic."""
        self.assertEqual(evenly_divisible_digits(12), 2)
        self.assertEqual(evenly_divisible_digits(223), 0)
        self.assertEqual(evenly_divisible_digits(1012), 3)
