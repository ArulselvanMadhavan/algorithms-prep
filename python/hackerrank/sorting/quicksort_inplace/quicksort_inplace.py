"""Pure Python."""
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/" + "../.."))
from utils import printutils


def partition(low, high, arr):
    """Parition in place."""
    pivot = arr[high - 1]
    indexForPivot = low
    for runner in range(low, high - 1):
        if arr[runner] <= pivot:
            swap(indexForPivot, runner, arr)
            indexForPivot += 1
    swap(indexForPivot, high - 1, arr)
    if (high - low) > 1:
        printutils.print_list_in_line(arr)
    return indexForPivot


def swap(source_index, dest_index, arr):
    """Swap source and dest."""
    temp = arr[source_index]
    arr[source_index] = arr[dest_index]
    arr[dest_index] = temp


def quicksort(low, high, arr):
    """Quicksort in place."""
    if low < high:
        pivotIndex = partition(low, high, arr)
        quicksort(low, pivotIndex, arr)
        quicksort(pivotIndex + 1, high, arr)

if __name__ == '__main__':
    n = int(input().strip().split(" ")[0])
    arr = [int(i) for i in input().strip().split(" ")]
    quicksort(0, n, arr)
