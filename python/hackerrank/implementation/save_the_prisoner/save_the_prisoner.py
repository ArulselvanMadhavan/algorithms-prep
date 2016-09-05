"""Pure Python."""
import unittest


def get_last_prisoner_id(num_prisoners, num_sweets, start_id):
    """Get Prisoner Id."""
    result = ((num_sweets + start_id) - 1) % num_prisoners
    if result == 0:
        return num_prisoners
    else:
        return result

if __name__ == '__main__':
    test_cases = int(input().strip().split(" ")[0])
    for test_case in range(test_cases):
        n, k, p = input().strip().split(" ")
        n, k, p = int(n), int(k), int(p)
        print(get_last_prisoner_id(n, k, p))


class TestLastPrisonerId(unittest.TestCase):
    """Prison Class."""

    def test_basic(self):
        """Basic Tests."""
        self.assertEqual(get_last_prisoner_id(5, 2, 1), 2)
