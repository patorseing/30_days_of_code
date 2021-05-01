#include "gtest/gtest.h"
#include "Solution.hpp"

using namespace std;

TEST(CaseIShould, ReturnCaseI)
{
  int n = 4;
  vector<string> arr_temp = split_string("1 4 3 2");
  vector<int> arr(n);

  for (int i = 0; i < n; i++)
  {
    int arr_item = stoi(arr_temp[i]);

    arr[i] = arr_item;
  }

  string actual = solve(arr);
  string expected = "2 3 4 1 ";
  EXPECT_EQ(expected, actual);
}
