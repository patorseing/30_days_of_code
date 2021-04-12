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

  public static String solve(int n,int i) {
    return n + " x " + i + " = " + n * i;
  }
  public static void main(String[] args) {
    int n = scanner.nextInt();
    scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
    for (int i = 1; i < 11; i++) {
      System.out.println(solve(n,i));
    }
    scanner.close();
  }

  @Test
  public void testSolveI() {
    String expected = "2 x 1 = 2";
    String actual = solve(2,1);
    assertEquals(expected, actual);
  }

  @Test
  public void testSolveII() {
    String expected = "2 x 2 = 4";
    String actual = solve(2,2);
    assertEquals(expected, actual);
  }
}
