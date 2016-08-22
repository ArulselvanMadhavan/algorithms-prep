package arul.algorithms.clrs.chapter2;

import java.io.*;
import java.util.stream.Collectors;

/**
 * Created by arulselvanmadhavan on 6/1/16.
 */
public class InsertionSort {

    protected int[] sort(int[] numbers) {
        for(int i = 1;i < numbers.length;i++){
            int current = i;
            for(int prev = current - 1;prev >= 0;prev--){
                if(numbers[current] > numbers[prev]){
                    break;
                } else {
                    int temp = numbers[current];
                    numbers[current] = numbers[prev];
                    numbers[prev] = temp;
                    current--;
                }
            }
        }
        return numbers;
    }

//    public static void main(String[] args) throws IOException {
//        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
//            System.out.println("Enter the numbers:(Ex: 2 4 11 3 4)");
//            String[] inputString = br.readLine().split(" ");
//            int[] inputIntegers = new int[inputString.length];
//            for (int i = 0; i < inputString.length; i++) {
//                inputIntegers[i] = Integer.parseInt(inputString[i]);
//            }
//            InsertionSort ins_obj = new InsertionSort();
//            ins_obj.sort(inputIntegers);
//        }
//    }
}
