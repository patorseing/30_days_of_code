#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

#include "Solution.hpp"

int main()
{
  /* Enter your code here. Read input from STDIN. Print output to STDOUT */
  int T;
  vector<string> Slist;
  cin >> T;
  for (int i = 0; i < T; i++)
  {
    /* code */
    string S;
    cin >> S;
    Slist.push_back(S);
  }

  for (int i = 0; i < Slist.size(); i++)
  {
    auto [str1, str2] = solve(Slist, i);
    cout << str1 << " ";
    cout << str2 << endl;
  }

  return 0;
}
