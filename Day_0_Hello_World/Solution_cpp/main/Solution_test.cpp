#include "gtest/gtest.h"
#include "Solution.hpp"

using namespace std;

TEST(ConcatShould, ReturnConcat)
{
  string expected = "Hello, World. \nWelcome to 30 Days of Code!";
  string actual = concat("Welcome to 30 Days of Code!");
  EXPECT_EQ(expected, actual);
}
