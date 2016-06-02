package arul.algorithms.clrs.chapter2;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 * Created by arulselvanmadhavan on 6/1/16.
 */
public class InsertionSortTest {
    InsertionSort obj = new InsertionSort();

    @Test
    public void printTestMessage(){
//        assertArrayEquals(new int[]{2,3,4,5},obj.sort(new int[]{5,2,4,3}));
        assertArrayEquals(new int[]{-1,0,0,1,5},obj.sort(new int[]{0,0,1,5,-1}));
    }
}
