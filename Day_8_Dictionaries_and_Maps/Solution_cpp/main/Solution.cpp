#include "Solution.hpp"

using namespace std;

int main()
{
  /* Enter your code here. Read input from STDIN. Print output to STDOUT */
  int n;
  cin >> n;
  // empty map container
  map<string, int> phoneBook;
  vector<string> searches;

  for (int i = 0; i < n; i++)
  {
    // insert elements in random order
    string name;
    cin >> name;

    int number;
    cin >> number;
    insert(phoneBook, name, number);
  }
  string search;
  while (cin >> search)
  {
    // searches.push_back(search);
    cout << find(phoneBook, search) << endl;
  }
  return 0;
}
