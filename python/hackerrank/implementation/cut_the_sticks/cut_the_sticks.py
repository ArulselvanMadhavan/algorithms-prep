"""Pure Python."""
import unittest


def cut_the_sticks(arr, n):
    """Cut Sticks."""
    arr.sort(reverse=True)
    result = []
    while len(arr) > 0:
        result.append(len(arr))
        block_cut = arr.pop()
        while len(arr) > 0 and arr[-1] <= block_cut:
            arr.pop()
    return result

if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    result = cut_the_sticks(arr, n)
    for val in result:
        print(val)


class TestCutSticks(unittest.TestCase):
    """Test."""

    def test_basic(self):
        """Basic Test cases."""
        self.assertEqual(cut_the_sticks([5, 4, 4, 2, 2, 8], 6), [6, 4, 2, 1])
        self.assertEqual(cut_the_sticks([1, 2, 3, 4, 3, 3, 2, 1], 8),
                            [8, 6, 4, 1])
