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
  public static void main(String[] args) throws IOException {
    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

    int n = Integer.parseInt(bufferedReader.readLine().trim());

    bufferedReader.close();

    System.out.println(solve(n));
  }

  public static int solve(int dec) {
    String bin = "";

    int count = 0;
    int MaxCount = 0;

    while (dec > 0) {
      if (dec % 2 == 0) {
        if (MaxCount < count) {
          MaxCount = count;
        }

        count = 0;
        bin.concat("0");
      } else {
        count += 1;
        bin.concat("1");
      }
      dec >>= 1;
    }
    if (MaxCount < count) {
      MaxCount = count;
    }
    return MaxCount;
  }

  @Test
  public void testI() {
    int n = 5;
    int expected = 1;
    int actual = solve(n);
    assertEquals(expected, actual);
  }

  @Test
  public void testII() {
    int n = 13;
    int expected = 2;
    int actual = solve(n);
    assertEquals(expected, actual);
  }
}
