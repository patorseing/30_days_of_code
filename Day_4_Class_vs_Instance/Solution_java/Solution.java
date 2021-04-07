import java.io.*;
import java.util.*;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Solution {

  public class Person {
    private int age;

    public Person(int initialAge) {
      // Add some more code to run some checks on initialAge
      if (initialAge < 0) {
        System.out.println("Age is not valid, setting age to 0.");
      } else {
        this.age = initialAge;
      }
    }

    public String amIOldLogic() {
      // Write code determining if this person's age is old and print the correct
      // statement:
      String str = "";
      if (this.age < 0) {
        str = "Age is not valid, setting age to 0.";
      } else if (this.age < 13) {
        str = "You are young.";
      } else if (this.age >= 13 && this.age < 18) {
        str = "You are a teenager.";
      } else {
        str = "You are old.";
      }
      return str;
    }

    public void amIOld() {
      // Write code determining if this person's age is old and print the correct
      // statement:
      System.out.println(this.amIOldLogic());
    }

    public void yearPasses() {
      // Increment this person's age.
      ++this.age;
    }
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int T = sc.nextInt();
    for (int i = 0; i < T; i++) {
      int age = sc.nextInt();
      Solution solution = new Solution();
      Solution.Person p = solution.new Person(age);
      p.amIOld();
      for (int j = 0; j < 3; j++) {
        p.yearPasses();
      }
      p.amIOld();
      System.out.println();
    }
    sc.close();
  }

  @Test
  public void testPersonCaseI() {
    int age = -1;
    Solution solution = new Solution();
    Solution.Person p = solution.new Person(age);
    String expected = "You are young.";
    String actual = p.amIOldLogic();
    assertEquals(expected, actual);

    for (int j = 0; j < 3; j++) {
      p.yearPasses();
    }

    expected = "You are young.";
    actual = p.amIOldLogic();
    assertEquals(expected, actual);
  }

  @Test
  public void testPersonCaseII() {
    int age = 10;
    Solution solution = new Solution();
    Solution.Person p = solution.new Person(age);
    String expected = "You are young.";
    String actual = p.amIOldLogic();
    assertEquals(expected, actual);

    for (int j = 0; j < 3; j++) {
      p.yearPasses();
    }

    expected = "You are a teenager.";
    actual = p.amIOldLogic();
    assertEquals(expected, actual);
  }

  @Test
  public void testPersonCaseIII() {
    int age = 16;
    Solution solution = new Solution();
    Solution.Person p = solution.new Person(age);
    String expected = "You are a teenager.";
    String actual = p.amIOldLogic();
    assertEquals(expected, actual);

    for (int j = 0; j < 3; j++) {
      p.yearPasses();
    }

    expected = "You are old.";
    actual = p.amIOldLogic();
    assertEquals(expected, actual);
  }

  @Test
  public void testPersonCaseIV() {
    int age = 18;
    Solution solution = new Solution();
    Solution.Person p = solution.new Person(age);
    String expected = "You are old.";
    String actual = p.amIOldLogic();
    assertEquals(expected, actual);

    for (int j = 0; j < 3; j++) {
      p.yearPasses();
    }

    expected = "You are old.";
    actual = p.amIOldLogic();
    assertEquals(expected, actual);
  }
}
