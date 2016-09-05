"""Pure Python."""
import itertools
import unittest
from functools import reduce


def next_lexicographically_greater_perm(input_str):
    """Next greater perm."""
    arr = list(input_str)
    i = len(arr) - 1
    # Find the first non-increasing suffix
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return "no answer"
    # i - 1 => contains the first decreasing suffix
    # i => contains the starting of the increasing suffix
    # j => First suffix that is greater than i -1
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # Reverse the suffix
    arr[i:] = arr[len(arr) - 1: i - 1: -1]
    return "".join(arr)


def lexicographically_greater_worst(input_str):
    """Lexicographically greater string."""
    input_as_tuple = tuple(input_str)

    def filter_lexicographically_greater(str_tuple):
        """Filter."""
        return str_tuple > input_as_tuple
    permutations = itertools.permutations(input_str)
    filtered_perm = filter(filter_lexicographically_greater, permutations)
    next_val = next(filtered_perm, None)
    if next_val is None:
        return "no answer"
    else:
        final_perm = reduce(min, filtered_perm, next_val)
        return ''.join(final_perm)

if __name__ == '__main__':
    num_testcases = int(input().strip())
    for test_case in range(num_testcases):
        input_str = input().strip()
        final_str = next_lexicographically_greater_perm(input_str)
        print(final_str)


class TestLexicographicallyGreater(unittest.TestCase):
    """Some class."""

    def test_basic(self):
        """Basic tests."""
        self.assertEqual(next_lexicographically_greater_perm("ab"), "ba")
        self.assertEqual(next_lexicographically_greater_perm("bb"),
                         "no answer")
        self.assertEqual(next_lexicographically_greater_perm("hefg"), "hegf")
        self.assertEqual(next_lexicographically_greater_perm("dhck"), "dhkc")
        self.assertEqual(next_lexicographically_greater_perm("dkhc"), "hcdk")
