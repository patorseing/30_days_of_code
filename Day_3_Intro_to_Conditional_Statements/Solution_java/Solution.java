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
    int N = scanner.nextInt();
    scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

    scanner.close();

    System.out.println(calWeird(N));
  }

  public static String calWeird(int N) {
    String result = "";
    if (N % 2 == 1) {
      result = "Weird";
    } else {
      if (N > 1 && N < 6) {
        result = "Not Weird";
      } else if (N > 5 && N < 21) {
        result = "Weird";
      } else {
        result = "Not Weird";
      }
    }
    return result;
  }

  @Test
  public void testCalWeird() {
    String expected = "Weird";
    String actual = calWeird(3);
    assertEquals(expected, actual);
  }

  @Test
  public void testCalNotWeird() {
    String expected = "Not Weird";
    String actual = calWeird(24);
    assertEquals(expected, actual);
  }
}
