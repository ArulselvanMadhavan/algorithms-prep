"""Pure Python."""
import unittest


def length_of_subset(arr, n, k):
    """Length of non-divisble subset."""
    count = [0] * k
    for i in range(n):
        count[arr[i] % k] += 1
    final_count = min(count[0], 1)
    for i in range(1, k//2 + 1):
        if i != k - i:
            final_count += max(count[i], count[k - i])
    if k % 2 == 0:
        final_count += 1
    return final_count

if __name__ == '__main__':
    n, k = input().strip().split(" ")
    n = int(n)
    k = int(k)
    arr = input().strip().split(" ")
    for v in range(len(arr)):
        arr[v] = int(arr[v])
    print(length_of_subset(arr, n, k))


class TestNonDivisibleSubsetLength(unittest.TestCase):
    """Test Class."""

    def test_basic(self):
        """Basic Test function."""
        self.assertEqual(length_of_subset([1, 7, 2, 4], 4, 3), 3)
