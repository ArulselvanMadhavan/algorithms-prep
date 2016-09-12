"""Pure Python."""


def print_list_in_line(arr):
    """Inline printing."""
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def insertion_sort(n, arr):
    """Main Insertion sort."""
    for i in range(1, n):
        insertion_sort_helper(i + 1, arr)
        print_list_in_line(arr)


def insertion_sort_helper(n, arr):
    """insertion_sort."""
    # 1. Empty the last slot
    # 2. Current pointer is 1 slot above the empty slot.
    # 3. Current pointer tries to find a replacement for the empty slot
    # 4. If cur_ptr is greater than value_to_sort, then empty the cur_ptr value
    # by moving the cur_ptr to the next slot
    # 5. print the array
    # Goto step 2
    # 6. If cur_ptr is lesser than value to sort, then replace the cur_ptr with
    # the value_to_sort
    value_to_sort = arr[n - 1]
    for cur_ptr in range(n - 2, -1, -1):
        if arr[cur_ptr] > value_to_sort:
            arr[cur_ptr + 1] = arr[cur_ptr]
        else:
            arr[cur_ptr + 1] = value_to_sort
            break
    if value_to_sort < arr[0]:
        arr[0] = value_to_sort


if __name__ == '__main__':
    n = int(input().strip())
    result = [int(val) for val in input().strip().split(" ")]
    insertion_sort(n, result)
