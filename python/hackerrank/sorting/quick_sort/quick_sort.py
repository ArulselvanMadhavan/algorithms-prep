"""Pure Python."""


def print_list_in_line_no_newline(arr):
    """No Newline."""
    for i in range(len(arr)):
        print(arr[i], end=" ")


def print_list_in_line(arr):
    """Inline printing."""
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def partition(n, arr):
    """Parition array."""
    pivot = arr[0]
    left, right, equal = [], [], []
    for i in range(n):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] > pivot:
            right.append(arr[i])
        else:
            equal.append(arr[i])
    return left, equal, right


def quick_sort(n, arr):
    if n <= 1:
        return arr
    else:
        left, equal, right = partition(n, arr)
        left = quick_sort(len(left), left)
        equal = quick_sort(len(equal), equal)
        right = quick_sort(len(right), right)
        result = (left + equal + right)
        print_list_in_line(result)
        return result

if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(val) for val in input().strip().split(" ")]
    quick_sort(n, arr)
