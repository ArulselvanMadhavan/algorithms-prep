"""Pure Python."""


def can_meet(x1, v1, x2, v2):
    """Can Kangaroos meet."""
    if x1 == x2 and v1 == v2:
        return "YES"
    elif x1 == x2 and v1 > v2:
        return "NO"
    elif x1 <= x2 and v1 <= v2:
        return "NO"
    else:
        if (x2 - x1) % (v1 - v2) == 0:
            return "YES"
        else:
            return "NO"

if __name__ == '__main__':
    x1, v1, x2, v2 = input().strip().split(' ')
    x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
    print(can_meet(x1, v1, x2, v2))
