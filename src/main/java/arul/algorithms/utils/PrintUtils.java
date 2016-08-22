package arul.algorithms.utils;

/**
 * Created by arulselvanmadhavan on 6/2/16.
 */
public class PrintUtils {
    public static void printIntArray(int[] array,String printFormat){
        for(int i=0;i<array.length;i++){
            System.out.printf(printFormat,array[i]);
        }
    }
}
