"""Pure Python."""
import unittest


def get_counter_value(time_val):
    """Counter value."""
    i = 0
    total_counter_val = (3 * 2**i)
    while (time_val > total_counter_val):
        i += 1
        total_counter_val = total_counter_val + (3 * 2**i)
    return (total_counter_val - time_val) + 1

if __name__ == '__main__':
    t = int(input().strip())


class TestCounterValue(unittest.TestCase):
    """Test class."""

    def test_basic(self):
        """Basic."""
        self.assertEqual(get_counter_value(3), 1)
        self.assertEqual(get_counter_value(4), 6)
        self.assertEqual(get_counter_value(21), 1)
