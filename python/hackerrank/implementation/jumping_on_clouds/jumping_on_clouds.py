"""Pure Python."""
import unittest


def get_min_jumps(arr, n):
    """Get min jumps."""
    cur_pos = 0
    count = 0
    while cur_pos < (n - 1):
        if (cur_pos + 2) < n and arr[cur_pos + 2] != 1:
            cur_pos += 2
        else:
            cur_pos += 1
        count += 1
    return count

if __name__ == '__main__':
    n = int(input().strip())
    c = [int(c_temp) for c_temp in input().strip().split(' ')]
    print(get_min_jumps(c, n))


class TestMinJumpsCount(unittest.TestCase):
    """Test."""

    def test_basic(self):
        """Basic test."""
        self.assertEqual(get_min_jumps([0, 0, 0, 0, 1, 0], 6), 3)
        self.assertEqual(get_min_jumps([0, 0, 1, 0, 0, 1, 0], 7), 4)
