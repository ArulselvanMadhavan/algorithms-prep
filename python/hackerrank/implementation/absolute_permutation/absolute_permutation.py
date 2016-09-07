"""Pure Python."""
import unittest


def smallest_abs_permutation(n, k):
    """Smallest abs permutation."""
    used_arr = [0] * n
    track_out = [0] * n
    for pos in range(1, n+1):
        if (pos - k) > 0 and used_arr[pos - k - 1] != 1:
            track_out[pos - 1] = pos - k
            used_arr[pos - k - 1] = 1
        elif (pos + k) <= n and used_arr[pos + k - 1] != 1:
            track_out[pos - 1] = pos + k
            used_arr[pos + k - 1] = 1
        else:
            return [-1]
    return track_out

if __name__ == '__main__':
    t = int(input().strip())
    for a0 in range(t):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        result = smallest_abs_permutation(n, k)
        for pos in range(len(result)):
            print(result[pos], end=" ")
        print()


class TestAbsolutePerm(unittest.TestCase):
    """Test Absolute Perm."""

    def test_basic(self):
        """Basic."""
        self.assertEqual(smallest_abs_permutation(2, 1), [2, 1])
        self.assertEqual(smallest_abs_permutation(3, 0), [1, 2, 3])
        self.assertEqual(smallest_abs_permutation(3, 2), -1)
