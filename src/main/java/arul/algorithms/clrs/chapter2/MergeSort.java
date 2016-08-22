package arul.algorithms.clrs.chapter2;

import arul.algorithms.utils.PrintUtils;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

/**
 * Created by arulselvanmadhavan on 6/1/16.
 */
public class MergeSort {
    private void merge(int[] numbers, int start, int mid, int end) {
        /**
         * Divide the numbers into sub-arrays namely,left and right
         * ex;[3,2]
         * Merge loop
         * [2,3,4,5,6]
         * L:[2,3] R:[4,5,6]
         * Loop invariant : The smallest of the left and right subarrays is moved into the final array
         */
        int[] left = new int[mid - start];
        int[] right = new int[end - mid];
        for (int i = 0; start + i < mid; i++) {
            left[i] = numbers[i];
        }
        for (int i = 0; mid + i < end; i++) {
            right[i] = numbers[mid + i];
        }
        int leftPtr = 0, rightPtr = 0;
        for (int i = 0; i < end; i++) {
            if (leftPtr == left.length) {
                while(rightPtr != right.length) {
                    numbers[i] = right[rightPtr];
                    rightPtr++;
                }
                break;
            } else if (rightPtr == right.length) {
                while(leftPtr != left.length) {
                    numbers[i] = left[leftPtr];
                    leftPtr++;
                }
                break;
            } else if (left[leftPtr] < right[rightPtr]) {
                numbers[i] = left[leftPtr];
                leftPtr++;
            } else {
                numbers[i] = right[rightPtr];
                rightPtr++;
            }
        }
    }

    private void merge_sort(int[] numbers, int start,int end){
        if (start < end) {
            int mid = (start + end) / 2;
            merge_sort(numbers, start, mid);
            merge_sort(numbers, mid + 1, end);
            merge(numbers, start, mid, end);
        }
    }
    /**
     * Recursion
     * array, start,end
     * divide the array into 2
     * recurse on the left and right array
     * recursion terminates when start is less than end
     *
     * @param numbers
     */
    protected int[] sort(int[] numbers) {
        merge_sort(numbers,0,numbers.length);
        return numbers;
    }

//    public static void main(String[] args) throws IOException {
//        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
//
//        }
//    }
}
