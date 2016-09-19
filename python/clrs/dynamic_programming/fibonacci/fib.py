"""Pure Python."""
import unittest


def fib_dp(n):
    """Compute Fib."""
    result = [0] * (n + 1)
    result[1] = 1
    for i in range(2, n + 1):
        result[i] = result[i - 1] + result[i - 2]
    return result


class TestFib(unittest.TestCase):
    """Some test."""

    def test_basic(self):
        """Basic."""
        self.assertEqual(fib_dp(3), [0, 1, 1, 2])
        self.assertEqual(fib_dp(4), [0, 1, 1, 2, 3])
        self.assertEqual(fib_dp(5), [0, 1, 1, 2, 3, 5])
        self.assertEqual(fib_dp(6), [0, 1, 1, 2, 3, 5, 8])
