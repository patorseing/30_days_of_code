using namespace std;

int solve(int dec)
{
  std::string bin{};
  int count = 0;
  int MaxCount = 0;

  while (dec > 0)
  {
    if (dec % 2 == 0)
    {
      if (MaxCount < count)
      {
        MaxCount = count;
      }

      count = 0;
      bin.insert(bin.begin(), '0');
    }
    else
    {
      count += 1;
      bin.insert(bin.begin(), '1');
    }

    dec >>= 1;
  }

  if (MaxCount < count)
  {
    MaxCount = count;
  }
  return MaxCount;
}
