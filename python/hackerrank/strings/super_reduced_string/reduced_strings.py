"""Pure Python."""
import unittest


def reduced_string(some_str):
    """Return the reduced_string."""
    reduced_str = []
    input_str = list(some_str)
    i = 0
    input_len = len(input_str)
    while i < input_len:
        # print("{}\t{}".format(i, input_str[i]))
        if i + 1 < input_len and input_str[i] == input_str[i + 1]:
            # print("next equal {}".format(i))
            i += 1  # Skip the char
        elif len(reduced_str) != 0 and input_str[i] == reduced_str[-1]:
            # print("prev_equal {}".format(i))
            reduced_str.pop()
        else:
            # print("Adding to reduced_str {}".format(i))
            reduced_str.append(input_str[i])
        i += 1
    if len(reduced_str) == 0:
        return "Empty String"
    else:
        return "".join(reduced_str)

if __name__ == '__main__':
    some_val = reduced_string(input().strip())
    print(some_val)


class TestReducedString(unittest.TestCase):
    """Reduced String."""

    def test_basic(self):
        """Basic tests."""
        self.assertEqual(reduced_string("aaabccddd"), "abd")
        self.assertEqual(reduced_string("baab"), "Empty String")
