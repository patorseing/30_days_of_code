import java.io.*;
import java.util.*;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Solution {

  private static final Scanner scanner = new Scanner(System.in);

  public static void main(String[] args) {
    /*
     * Enter your code here. Read input from STDIN. Print output to STDOUT. Your
     * class should be named Solution.
     */
    int T = scanner.nextInt();
    String[] Slist = new String[10];
    scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
    for (int i = 0; i < T; i++) {
      Slist[i] = scanner.nextLine();
    }

    for (int i = 0; i < T; i++) {
      String[] res = solve(Slist[i]);
      System.out.print(res[0]);
      System.out.println(res[1]);
    }
  }

  public static String[] solve(String str) {
    String first = "";
    String second = "";
    for (int j = 0; j < str.length(); j++) {
      if (j % 2 == 0) {
        first = first + str.charAt(j);
      } else {
        second = second + str.charAt(j);
      }
    }
    first += " ";
    String[] res = new String[] { first, second };
    return res;
  }

  @Test
  public void testSolveI() {
    String expected = "Hce akr";
    String[] res = solve("Hacker");
    String actual = res[0] + res[1];
    assertEquals(expected, actual);
  }

  @Test
  public void testSolveII() {
    String expected = "Rn ak";
    String[] res = solve("Rank");
    String actual = res[0] + res[1];
    assertEquals(expected, actual);
  }
}
