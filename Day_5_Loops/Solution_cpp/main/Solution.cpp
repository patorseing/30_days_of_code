#include "bits/stdc++.h"
#include "Solution.hpp"

using namespace std;



int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    for (int i = 1; i < 11; i++)
    {
      cout << solve(n, i) << endl;
    }

    return 0;
}
