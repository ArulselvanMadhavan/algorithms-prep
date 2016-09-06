"""Pure Python."""
import unittest


def special_problems_count(n, k, arr):
    """Special Problems Count."""
    current_page_no = 0
    special_problems = 0
    for chapter in range(n):
        num_pblms = arr[chapter]
        num_pages = num_pblms//k if num_pblms % k == 0 else (num_pblms//k) + 1
        problems_written = 0
        for _ in range(num_pages):
            current_page_no += 1
            pblms_to_be_written = min(num_pblms, k)
            if problems_written < current_page_no \
                    <= (problems_written+pblms_to_be_written):
                special_problems += 1
            problems_written += pblms_to_be_written
            num_pblms -= pblms_to_be_written
    return special_problems

if __name__ == '__main__':
    n, k = input().strip().split(" ")
    n, k = int(n), int(k)
    arr = [int(x) for x in input().strip().split(" ")]
    print(special_problems_count(n, k, arr))


class TestSpecialProblemsCount(unittest.TestCase):
    """Test Class."""

    def test_basic(self):
        """Basic."""
        self.assertEqual(special_problems_count(5, 3, [4, 2, 6, 1, 10]), 4)
