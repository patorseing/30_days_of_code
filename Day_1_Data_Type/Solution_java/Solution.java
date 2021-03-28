import static org.junit.Assert.assertEquals;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

import org.junit.Test;

public class Solution {

  public static String concat(String str) {
    return "HackerRank " + str;
  }

  public static int plusInt(int inInt) {
    int i = 4;
    return inInt + i;
  }

  public static double plusFloat(double inFloat) {
    double i = 4.0;
    return inFloat + i;
  }

  public static void main(String[] args) {
    int i = 4;
    double d = 4.0;
    String s = "HackerRank ";

    Scanner scan = new Scanner(System.in);

    /* Declare second integer, double, and String variables. */
    int input_i;
    double input_d;
    String input_string;

    /* Read and save an integer, double, and String to your variables. */
    // Note: If you have trouble reading the entire String, please go back and
    // review the Tutorial closely.
    input_i = scan.nextInt();
    input_d = scan.nextDouble();
    scan.nextLine(); // Consume newline left-over
    input_string = scan.nextLine();

    /* Print the sum of both integer variables on a new line. */
    // System.out.println(i + input_i);
    System.out.println(plusInt(input_i));

    /* Print the sum of the double variables on a new line. */
    // System.out.println(d + input_d);
    System.out.println(plusFloat(input_d));

    /*
     * Concatenate and print the String variables on a new line; the 's' variable
     * above should be printed first.
     */
    // System.out.println(s + input_string);
    System.out.println(concat(input_string));

    scan.close();
  }

  @Test
  public void testConcat() {
    String expected = "HackerRank is the best place to learn and practice coding!";
    String actual = concat("is the best place to learn and practice coding!");
    assertEquals(expected, actual);
  }

  @Test
  public void testPlusInt() {
    int expected = 16;
    int actual = plusInt(12);
    assertEquals(expected, actual);
  }

  @Test
  public void testPlusFloat() {
    double expected = 8.0;
    double actual = plusFloat(4.0);
    /*
     * assertEquals(expected, actual, delta) delta = expected - actual
     */
    assertEquals(expected, actual, 0.0);
  }
}
