"""Pure Python."""
import unittest


def is_cancelled(arr, n, threshold):
    """Check if class is cancelled."""
    late_count = 0
    for i in range(n):
        if arr[i] > 0:
            late_count += 1
    if (n - late_count) < threshold:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    t = int(input().strip())
    for a0 in range(t):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        a = [int(a_temp) for a_temp in input().strip().split(' ')]
        print(is_cancelled(a, n, k))


class TestHasClassMethod(unittest.TestCase):
    """Unit Test Class."""

    def test_basic(self):
        """Test Basic."""
        self.assertEqual(is_cancelled([-1, -3, 4, 2], 4, 3), "YES")
        self.assertEqual(is_cancelled([0, -1, 2, 1], 4, 2), "NO")
