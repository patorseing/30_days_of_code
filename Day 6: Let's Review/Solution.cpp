#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

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
    string first;
    string second;
    for (int j = 0; j < Slist[i].length(); j++)
    {
      if (j % 2 == 0)
      {
        first = first + Slist[i][j];
      }
      else
      {
        second = second + Slist[i][j];
      }
    }
    cout << first << " ";
    cout << second << endl;
  }

  return 0;
}
