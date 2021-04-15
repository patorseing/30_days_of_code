#include <tuple>

using namespace std;

tuple<string, string> solve(vector<string> Slist, int i)
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
  return {first, second};
}
