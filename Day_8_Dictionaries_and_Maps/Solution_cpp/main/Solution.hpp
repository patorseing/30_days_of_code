#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

void insert(map<string, int> phoneBook, string name, int number)
{
  phoneBook.insert(pair<string, int>(name, number));
}

string find(map<string, int> phoneBook, string search)
{
  string result = "";
  if (phoneBook.find(search) == phoneBook.end())
  {
    result = "Not found";
  }
  else
  {
    string name = phoneBook.find(search)->first;
    int number = phoneBook.find(search)->second;
    result = name + "=" + to_string(number);
  }
  return result;
}
