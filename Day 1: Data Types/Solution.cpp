#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;

int main()
{
  int i = 4;
  double d = 4.0;
  string s = "HackerRank ";

  // Declare second integer, double, and String variables.
  int input_i;
  double input_d;
  string input_string;

  // Read and save an integer, double, and String to your variables.
  // Note: If you have trouble reading the entire string, please go back and review the Tutorial closely.
  cin >> input_i;
  cin >> input_d;
  // eat whitespace
  getline(cin >> ws, input_string);

  // Print the sum of both integer variables on a new line.
  cout << i + input_i << endl;

  // Print the sum of the double variables on a new line.
  // Let's say we wanted to scale this to 1 decimal places:
  cout << fixed << setprecision(1) << d + input_d << endl;

  // Concatenate and print the String variables on a new line
  // The 's' variable above should be printed first.
  cout << s << input_string << endl;

  return 0;
}
