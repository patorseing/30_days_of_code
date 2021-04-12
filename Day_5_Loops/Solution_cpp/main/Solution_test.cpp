#include "gtest/gtest.h"
#include "Solution.hpp"

using namespace std;

TEST(CaseIShould, ReturnCaseI)
{
  string actual = solve(2, 1);
  string expected = "2 x 1 = 2";
  EXPECT_EQ(expected, actual);
}

TEST(CaseIIShould, ReturnCaseII)
{
  string actual = solve(2, 12);
  string expected = "2 x 12 = 24";
  EXPECT_EQ(expected, actual);
}

