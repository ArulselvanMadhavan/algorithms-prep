"""Pure Python."""
import unittest

# def rod_cutting(n, arr):
#     """Using DP."""
#     result = [[0] * (n + 1) for _ in range(n)]
#     for cut_size in range(1, n + 1):
#         for rod_len in range(1, n + 1):
#             if cut_size > rod_len:
#                 result[cut_size - 1][rod_len] = result[cut_size - 2][rod_len]
#             else:
#                 price_for_cut = arr[cut_size - 1]
#                 rem_price = result[cut_size - 1][rod_len - cut_size]
#                 result[cut_size - 1][rod_len] = price_for_cut + rem_price
#     return result

def rod_cutting(n, arr):
    """Using DP."""
    result = [0] * (n + 1)
    solution = [0] * (n + 1)
    for rod_length in range(1, n + 1):
        max_price = 0
        for cut_size in range(1, rod_length + 1):
            price_val = arr[cut_size - 1]
            rem_length = rod_length - cut_size
            total_price = price_val + result[rem_length]
            if total_price > max_price:
                max_price = total_price
                solution[rod_length] = cut_size
        result[rod_length] = max_price
    return result, solution


if __name__ == '__main__':
    n = int(input().strip().split(" ")[0])
    arr = [int(val) for val in input().strip().split(" ")]
    result, solution = rod_cutting(n, arr)
    print(result)
    print(solution)


class TestRodCutting(unittest.TestCase):
    """Test Class."""

    def test_basic(self):
        """basic tests."""
        result, solution = rod_cutting(10, [1, 5, 8, 9, 10, 17, 17, 20, 24, 30])
        self.assertEqual(result, [0, 1, 5, 8, 10, 13, 17, 18, 22, 25, 30])
        self.assertEqual(solution, [0, 1, 2, 3, 2, 2, 6, 1, 2, 3, 10])
