"""Pure Python."""
import unittest


def get_even_odd_count(n, arr):
    """Return even odd count."""
    mod_arr = [0] * n
    odd_count = 0
    for i in range(n):
        if arr[i] % 2 == 1:
            odd_count += 1
            mod_arr[i] = 1
    return odd_count, mod_arr


def get_min_ration_count(n, arr):
    """Fair Rations Count."""
    odd_count, mod_arr = get_even_odd_count(n, arr)
    if odd_count % 2 == 1:
        return "NO"
    else:
        last_odd_pos = -1
        min_count = 0
        for i in range(n):
            if mod_arr[i] == 1:
                if last_odd_pos != -1:
                    min_count += (i - last_odd_pos)
                    last_odd_pos = -1
                else:
                    last_odd_pos = i
        return (min_count * 2)

if __name__ == '__main__':
    N = int(input().strip())
    B = [int(B_temp) for B_temp in input().strip().split(' ')]
    print(get_min_ration_count(N, B))


class TestMinRationCount(unittest.TestCase):
    """Test."""

    def test_basic(self):
        """Basic."""
        self.assertEqual(get_min_ration_count(5, [2, 3, 4, 5, 6]), 4)
        self.assertEqual(get_min_ration_count(2, [1, 2]), "NO")
