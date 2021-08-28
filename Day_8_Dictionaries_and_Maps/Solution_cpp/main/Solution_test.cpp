#include "gtest/gtest.h"
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include "Solution.hpp"

using namespace std;

TEST(CaseFoundShould, ReturnCaseFound)
{
  map<string, int> phoneBook = {
      {"sam", 99912222},
      {"tom", 11122222},
      {"harry", 12299933}};

  string expected = "sam=99912222";
  string actual = find(phoneBook, "sam");

  EXPECT_EQ(expected, actual);
}

TEST(CaseNotFoundShould, ReturnCaseNotFound)
{
  map<string, int> phoneBook = {
      {"sam", 99912222},
      {"tom", 11122222},
      {"harry", 12299933}};

  string expected = "Not found";
  string actual = find(phoneBook, "edward");

  EXPECT_EQ(expected, actual);
}
