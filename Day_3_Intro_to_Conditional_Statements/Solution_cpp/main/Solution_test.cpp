#include "gtest/gtest.h"
#include "Solution.hpp"

using namespace std;

TEST(WeirdShould, ReturnWeird)
{
  string expected = "Weird";
  string actual = solve(3);
  EXPECT_EQ(expected, actual);
}

TEST(NotWeirdShould, ReturnNotWeird)
{
  string expected = "Not Weird";
  string actual = solve(24);
  EXPECT_EQ(expected, actual);
}
