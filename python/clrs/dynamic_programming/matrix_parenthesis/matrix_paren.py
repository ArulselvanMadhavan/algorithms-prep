"""Pure Python."""
import unittest


class Matrix(object):
    """Matrix order."""

    def __init__(self, x, y):
        """Contructor."""
        self.m = x
        self.n = y


def get_optimal_paren(n, arr):
    """Optimal Paren."""
    result = [[0] * n for i in range(n)]
    for chain_length in range(1, n):
        start_matrix = 0
        end_matrix = start_matrix + chain_length
        while end_matrix < n:
            print("{}\t{}".format(start_matrix + 1, end_matrix + 1))
            result[start_matrix][end_matrix] = get_min_cost(start_matrix,
                                                            end_matrix,
                                                            result,
                                                            arr)
            start_matrix += 1
            end_matrix += 1

    print(result)


def get_min_cost(start, end, result, arr):
    """Min Cost."""
    min_value = 999999
    for k in range(start, end):
        print("{}\t{}\t{}".format(start, k, end))
        cur_val = result[start][k] + result[k + 1][end] \
                                   + get_cost(start - 1, k, end, arr)
        if cur_val < min_value:
            min_value = cur_val
    return min_value


def get_cost(i, j, k, arr):
    """Cost."""
    return arr[i].n * arr[j].n * arr[k].n

if __name__ == '__main__':
    n = int(input().strip().split(" ")[0])
    arr = [Matrix] * n
    for i in range(n):
        matrix_order = input().strip().split(" ")
        matr_obj = Matrix(int(matrix_order[0]), int(matrix_order[1]))
        arr[i] = matr_obj
    get_optimal_paren(n, arr)


class TestMatrixParenthesis(unittest.TestCase):
    """Test."""

    def test_basic(self):
        """Test get cost."""
        arr = [Matrix(4, 5), Matrix(5, 6), Matrix(6, 7)]
        self.assertEqual(get_cost(0, 1, 2, arr), 4 * 5 * 6 * 7)

    def test_get_min_cost(self):
        self.assertEqual()
