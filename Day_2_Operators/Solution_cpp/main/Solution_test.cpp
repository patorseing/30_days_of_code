#include "gtest/gtest.h"
#include "Solution.hpp"

using namespace std;

TEST(SolveShould, ReturnSolve)
{
  int expected = 15;
  int actual = solve(12.00,20,8);
  EXPECT_EQ(expected, actual);
}
