import java.io.*;
import java.util.*;

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
      String first = "";
      String second = "";
      for (int j = 0; j < Slist[i].length(); j++) {
        if (j % 2 == 0) {
          first = first + Slist[i].charAt(j);
        } else {
          second = second + Slist[i].charAt(j);
        }
      }
      first += " ";
      System.out.print(first);
      System.out.println(second);
    }
  }
}
