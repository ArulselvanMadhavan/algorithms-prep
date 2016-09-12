"""Pure Python."""


def print_list_in_line(arr):
    """Inline printing."""
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def print_list_in_line_no_newline(arr):
    """No Newline."""
    for i in range(len(arr)):
        print(arr[i], end=" ")
