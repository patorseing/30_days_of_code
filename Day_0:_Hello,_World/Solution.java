import static org.junit.Assert.assertEquals;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

import org.junit.Test;

public class Solution {

	public static String concat(String str) {
		return "Hello, World. \n"+str;
	}

	public static void main(String[] args) {
		// Create a Scanner object to read input from stdin.
		Scanner scan = new Scanner(System.in);

		// Read a full line of input from stdin and save it to our variable,
		// inputString.
		String inputString = scan.nextLine();

		// Close the scanner object, because we've finished reading
		// all of the input from stdin needed for this challenge.
		scan.close();
		String result = concat(inputString);
		System.out.println(result);
		// Print a string literal saying "Hello, World." to stdout.
		// System.out.println("Hello, World.");

		// TODO: Write a line of code here that prints the contents of inputString to
		// stdout.
		// System.out.println(inputString);
	}

	@Test
	public void testConcat(){
		String expected = "Hello, World. \nWelcome to 30 Days of Code!";
		String actual = concat("Welcome to 30 Days of Code!");
		assertEquals(expected, actual);
	}
}
