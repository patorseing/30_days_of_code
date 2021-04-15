#include "gtest/gtest.h"
#include "Solution.hpp"

using namespace std;

TEST(CaseIShould, ReturnCaseI)
{
  auto [actualstr1, actualstr2] = solve({"Hacker", "Rank"}, 0);
  string expectedstr1 = "Hce";
  string expectedstr2 = "akr";
  EXPECT_EQ(expectedstr1, actualstr1);
  EXPECT_EQ(expectedstr2, actualstr2);
}

TEST(CaseIIShould, ReturnCaseII)
{
  auto [actualstr1, actualstr2] = solve({"Hacker", "Rank"}, 1);
  string expectedstr1 = "Rn";
  string expectedstr2 = "ak";
  EXPECT_EQ(expectedstr1, actualstr1);
  EXPECT_EQ(expectedstr2, actualstr2);
}

