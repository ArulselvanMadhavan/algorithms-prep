package arul.algorithms.clrs.chapter2;
import arul.algorithms.utils.PrintUtils;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 * Created by arulselvanmadhavan on 6/2/16.
 */
public class MergeSortTest {
    MergeSort obj = new MergeSort();

    @Test
    public void test(){
        int[] test1 = new int[]{4,7,6,2,0};
        PrintUtils.printIntArray(obj.sort(test1),"%d\t");
//        assertArrayEquals(new int[]{0,2,4,6,7},obj.sort(test1));
    }
}
