"""Pure Python."""
import unittest


def max_distance_old(n, m, arr):
    """Max distance."""
    max_dist = 0
    for city in range(n):
        dist_from_city = min(map(lambda x: abs(city - x), arr))
        if max_dist < dist_from_city:
            max_dist = dist_from_city
    return max_dist


def get_max_btw_distance(m, arr):
    """Get Max Btw dist."""
    max_btw_dist = 0
    for i in range(m - 1):
        temp = arr[i + 1] - arr[i]
        temp = temp//2 if temp % 2 == 0 else (temp - 1)//2
        if temp > max_btw_dist:
            max_btw_dist = temp
    return max_btw_dist


def max_distance(n, m, arr):
    """New."""
    arr.sort()
    left_max = abs(0 - arr[0])
    right_max = abs((n - 1) - arr[m - 1])
    btw_max = get_max_btw_distance(m, arr)
    max_dist = max((left_max, right_max, btw_max))
    return max_dist

if __name__ == '__main__':
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    c = [int(c_temp) for c_temp in input().strip().split(' ')]
    print(max_distance(n, m, c))


class TestMaxDistance(unittest.TestCase):
    """Test Max Distance."""

    def test_basic(self):
        """Basic."""
        self.assertEqual(max_distance(6, 6, [0, 1, 2, 4, 3, 5]), 0)
        self.assertEqual(max_distance(5, 2, [0, 4]), 2)
        self.assertEqual(max_distance(10, 2, [3, 9]), 3)
        self.assertEqual(max_distance(10, 1, [3]), 6)
        self.assertEqual(max_distance(11, 2, [4, 10]), 4)
