"""Pure Python."""


def rod_cutting(n, arr):
    """Return max profit."""
    result = [0] * n
    for cut_length in range(n, 0, -1):
        rem_length = n - cut_length
        value_from_cut = arr[cut_length - 1]
        rem_value = 0
        if rem_length > 0:
            rem_value = rod_cutting(rem_length, arr)
        result[rem_length] = value_from_cut + rem_value
    return max(result)

if __name__ == '__main__':
    n = int(input().strip().split(" ")[0])
    arr = [int(val) for val in input().strip().split(" ")]
    result = rod_cutting(n, arr)
    print(result)
