#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
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
    phoneBook.insert(pair<string, int>(name, number));
  }
  string search;
  while (cin >> search)
  {
    // searches.push_back(search);
    if (phoneBook.find(search) == phoneBook.end())
    {
      cout << "Not found" << endl;
    }
    else
    {
      cout << phoneBook.find(search)->first << "=" << phoneBook.find(search)->second << endl;
    }
  }
  return 0;
}
