#include <bits/stdc++.h>

using namespace std;

int main()
{
  int n;
  cin >> n;
  cin.ignore(numeric_limits<streamsize>::max(), '\n');

  int count = 0;
  int max = 0;

  while (n > 0)
  {
    if (n % 2 == 1)
    {
      count++;
      n = (n - 1) / 2;
      // cout << n << " " << 1 << " " << count << "\n";
    }
    else
    {
      count = 0;
      n = n / 2;
      // cout << n << " " << 0 << " " << count << "\n";
    }
    if (count >= max)
    {
      max = count;
    }
  }
  cout << max << "\n";
  return 0;
}
