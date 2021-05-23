#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>

#include <string>
#include <fstream>

using namespace std;

void tokenize(string &str, char delim, vector<string> &out)
{
  size_t start;
  size_t end = 0;

  while ((start = str.find_first_not_of(delim, end)) != string::npos)
  {
    end = str.find(delim, start);
    out.push_back(str.substr(start, end - start));
  }
}

int main()
{
  /* Enter your code here. Read input from STDIN. Print output to STDOUT */
  ifstream inFile, secFile;
  inFile.open("testcase.txt");
  secFile.open("result.txt");
  int n;
  map<string, int> phoneBook;
  vector<string> searches;

  if (inFile.good())
  {
    string sLine;
    getline(inFile, sLine);
    n = std::stoi(sLine);
  }

  for (int i = 0; i < n; i++)
  {
    if (inFile.good())
    {
      string sLine;
      getline(inFile, sLine);
      char d = ' ';
      vector<string> a;
      tokenize(sLine, d, a);
      string name = a[0];
      int number = std::stoi(a[1]);
      phoneBook.insert(pair<string, int>(name, number));
    }
  }
  // for (int i = 0; i < n; i++)
  // {
  //   // insert elements in random order
  //   if (inFile.good())
  //   {
  //     string search;
  //     getline(inFile, search);
  //     searches.push_back(search);
  //   }
  // }
  while (inFile.good())
  {
    string search;
    getline(inFile, search);
    searches.push_back(search);
  }

  inFile.close();
  int correct = 0, error = 0;
  int size = searches.size();
  cout << "size query: " << size << endl;
  for (int x = 0; x < size; x++)
  {
    if (secFile.good())
    {
      string res;
      getline(secFile, res);

      if (phoneBook.find(searches[x]) == phoneBook.end())
      {
        if (res == "Not found")
        {
          correct++;
        }
        else
        {
          cout << x << searches[x] << endl;
          cout << "Not found" << endl;
          cout << "True value: " << res << endl;
          error++;
        }
      }
      else
      {
        string str = to_string(phoneBook.find(searches[x])->second);
        string check = phoneBook.find(searches[x])->first + "=" + str;
        if (res == check)
        {
          correct++;
        }
        else
        {
          cout << phoneBook.find(searches[x])->first << "=" << phoneBook.find(searches[x])->second << endl;
          cout << "True value: " << res << endl;
        }
      }
    }
    else
    {
      error++;
    }
  }
  cout << "correct: " << correct << endl;
  cout << "error: " << error << endl;
  return 0;
}
