#include "gtest/gtest.h"
#include "Solution.hpp"

using namespace std;

TEST(CaseIShould, ReturnCaseI)
{
  int age = -1;
  Person p(age);
  string actual = p.amIOldLogic();
  string expected = "You are young.";
  EXPECT_EQ(expected, actual);
  for (int j = 0; j < 3; j++)
  {
    p.yearPasses();
  }
  actual = p.amIOldLogic();
  expected = "You are young.";
  EXPECT_EQ(expected, actual);
}

TEST(CaseIIShould, ReturnCaseII)
{
  int age = 10;
  Person p(age);
  string actual = p.amIOldLogic();
  string expected = "You are young.";
  EXPECT_EQ(expected, actual);
  for (int j = 0; j < 3; j++)
  {
    p.yearPasses();
  }
  actual = p.amIOldLogic();
  expected = "You are a teenager.";
  EXPECT_EQ(expected, actual);
}

TEST(CaseIIIShould, ReturnCaseIII)
{
  int age = 16;
  Person p(age);
  string actual = p.amIOldLogic();
  string expected = "You are a teenager.";
  EXPECT_EQ(expected, actual);
  for (int j = 0; j < 3; j++)
  {
    p.yearPasses();
  }
  actual = p.amIOldLogic();
  expected = "You are old.";
  EXPECT_EQ(expected, actual);
}

TEST(CaseIVShould, ReturnCaseIV)
{
  int age = 18;
  Person p(age);
  string actual = p.amIOldLogic();
  string expected = "You are old.";
  EXPECT_EQ(expected, actual);
  for (int j = 0; j < 3; j++)
  {
    p.yearPasses();
  }
  actual = p.amIOldLogic();
  expected = "You are old.";
  EXPECT_EQ(expected, actual);
}
