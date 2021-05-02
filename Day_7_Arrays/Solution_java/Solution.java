import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Solution {

  private static final Scanner scanner = new Scanner(System.in);

  public static void main(String[] args) {
    int n = scanner.nextInt();
    scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

    int[] arr = new int[n];

    String[] arrItems = scanner.nextLine().split(" ");
    scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

    for (int i = 0; i < n; i++) {
      int arrItem = Integer.parseInt(arrItems[i]);
      arr[i] = arrItem;
    }
    System.out.println(reverse(arr));

    scanner.close();
  }

  static String reverse(int[] arr) {
    String result = "";
    for (int i = arr.length - 1; i >= 0; i--) {
      result += arr[i] + " ";
    }
    return result;
  }

  @Test
  public void testSolveI() {
    String expected = "2 3 4 1 ";
    int[] arr = {1,4,3,2};
    String actual = reverse(arr);
    assertEquals(expected, actual);
  }
}
