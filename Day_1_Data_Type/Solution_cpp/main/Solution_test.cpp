#include "gtest/gtest.h"
#include "Solution.hpp"

using namespace std;

TEST(ConcatShould, ReturnConcat)
{
  string expected = "HackerRank is the best place to learn and practice coding!";
  string actual = concat("is the best place to learn and practice coding!");
  EXPECT_EQ(expected, actual);
}

TEST(PlusIntShould, ReturnPlusInt)
{
  int expected = 16;
  int actual = plusInt(12);
  EXPECT_EQ(expected, actual);
}

TEST(PlusFloatShould, ReturnFloatInt)
{
  double expected = 8.0;
  double actual = plusFloat(4.0);
  EXPECT_EQ(expected, actual);
}
