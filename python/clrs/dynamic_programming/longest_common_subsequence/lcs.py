"""Pure Python."""
import unittest


def lcs(input_str1, input_str2):
    """Return the length of the lcs."""
    input_len1 = len(input_str1)
    input_len2 = len(input_str2)
    input_str1 = list(input_str1)
    input_str2 = list(input_str2)
    c = [[0] * (input_len1 + 1) for i in range(input_len2 + 1)]
    b = [[0] * (input_len1 + 1) for i in range(input_len2 + 1)]
    for i in range(1, input_len2 + 1):
        for j in range(1, input_len1 + 1):
            char_i = input_str2[i - 1]
            char_j = input_str1[j - 1]
            if char_i == char_j:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "diag"
            elif c[i][j - 1] > c[i - 1][j]:
                c[i][j] = c[i][j - 1]
                b[i][j] = "left"
            else:
                c[i][j] = c[i - 1][j]
                b[i][j] = "up"
    print_solution(b, input_str2, input_str1, c[input_len2][input_len1])
    return c[input_len2][input_len1]


def print_solution(b, input_str1, input_str2, final_str_len):
    """Print the lcs."""
    row_len = len(b)
    col_len = len(b[0])
    final_str = [" "] * final_str_len
    i = row_len - 1
    j = col_len - 1
    while row_len > 0 and col_len > 0:
        if b[i][j] == "diag":
            final_str[final_str_len - 1] = input_str1[i - 1]
            final_str_len -= 1
            i -= 1
            j -= 1
        elif b[i][j] == "up":
            i -= 1
        elif b[i][j] == "left":
            j -= 1
        else:
            break
    print("".join(final_str))


if __name__ == '__main__':
    input_str = input().strip()
    print(lcs(input_str))


class TestLCS(unittest.TestCase):
    """Test."""

    def test_basic(self):
        """Basic."""
        self.assertEqual(lcs("bdcaba", "abcbdab"), 4)
