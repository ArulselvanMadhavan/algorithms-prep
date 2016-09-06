"""Pure Python."""
import unittest


def bribe_count(final_pos, n):
    """Bribe Count."""
    bribe_count = 0
    for i in range(n - 1, -1, -1):
        if (final_pos[i] - (i + 1)) > 2:
            return "Too chaotic"
        for j in range(max(0, final_pos[i] - 2), i):
            if final_pos[j] > final_pos[i]:
                bribe_count += 1
    return bribe_count

if __name__ == '__main__':
    T = int(input().strip())
    for a0 in range(T):
        n = int(input().strip())
        q = [int(q_temp) for q_temp in input().strip().split(' ')]
        bribe_count(q, n)


class TestBribeCount(unittest.TestCase):
    """Test BribeCount."""

    def test_basic(self):
        """Basic tests."""
        self.assertEqual(bribe_count([2, 1, 5, 3, 4], 5), 3)
        self.assertEqual(bribe_count([2, 5, 1, 3, 4], 5), "Too chaotic")
