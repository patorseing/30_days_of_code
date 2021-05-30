#include "gtest/gtest.h"
#include "Solution.hpp"

using namespace std;

TEST(CaseIShould, ReturnCaseI)
{
  int n = 5;
  int expected = 1;

  int actual = solve(n);
  EXPECT_EQ(expected, actual);
}

TEST(CaseIIShould, ReturnCaseII)
{
  int n = 13;
  int expected = 2;

  int actual = solve(n);
  EXPECT_EQ(expected, actual);
}
