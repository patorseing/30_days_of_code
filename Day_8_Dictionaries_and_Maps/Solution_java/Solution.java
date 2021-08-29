
//Complete this code or write your own from scratch
import java.util.*;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Solution {
  public static void main(String[] arg) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    Map<String, Integer> myMap = new HashMap<String, Integer>();
    for (int i = 0; i < n; i++) {
      String name = in.next();
      int phone = in.nextInt();
      // Write code here
      myMap.put(name, phone);
    }
    while (in.hasNext()) {
      String s = in.next();
      // Write code here
      System.out.println(findPhone(myMap, s));
    }
    in.close();
  }

  static String findPhone(Map<String, Integer> phoneBook, String name) {
    String phone = "";
    if (phoneBook.get(name) == null) {
      phone = "Not found";
    } else {
      phone = name + "=" + phoneBook.get(name);
    }
    return phone;
  }

  @Test
  public void testSolveI() {
    Map<String, Integer> myMap = new HashMap<String, Integer>();
    myMap.put("sam", 99912222);
    myMap.put("tom", 11122222);
    myMap.put("harry", 12299933);

    String expected = "sam=99912222";
    String actual = findPhone(myMap, "sam");
    assertEquals(expected, actual);
  }

  @Test
  public void testSolveII() {
    Map<String, Integer> myMap = new HashMap<String, Integer>();
    myMap.put("sam", 99912222);
    myMap.put("tom", 11122222);
    myMap.put("harry", 12299933);

    String expected = "Not found";
    String actual = findPhone(myMap, "edward");
    assertEquals(expected, actual);
  }
}
