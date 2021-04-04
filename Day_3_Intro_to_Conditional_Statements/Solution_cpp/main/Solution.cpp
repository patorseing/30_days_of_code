#include "bits/stdc++.h"
#include "Solution.hpp"

using namespace std;

int main()
{
    int N;
    cin >> N;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    cout << solve(N) << endl;

    return 0;
}
