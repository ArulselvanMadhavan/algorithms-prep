"""Pure Python."""
import unittest


def get_min_dist(n, A):
    """Get Minimum Distance."""
    pos_dict = {}
    min_dist = n + 1
    for i in range(n):
        if pos_dict.get(A[i], None) is not None:
            min_dist = min(min_dist, i - pos_dict[A[i]])
        pos_dict[A[i]] = i
    if min_dist == n + 1:
        return -1
    else:
        return min_dist

if __name__ == '__main__':
    n = int(input().strip())
    A = [int(A_temp) for A_temp in input().strip().split(' ')]
    print(get_min_dist(n, A))


class TestMinDist(unittest.TestCase):
    """Test."""

    def test_basic(self):
        """Basic."""
        self.assertEqual(get_min_dist(6, [7, 1, 3, 4, 1, 7]), 3)
        self.assertEqual(get_min_dist(6, [4, 4, 1, 3, 4, 6]), 1)
