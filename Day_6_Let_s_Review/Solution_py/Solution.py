# Enter your code here. Read input from STDIN. Print output to STDOUT

#!/bin/python3

import math
import os
import random
import re
import sys

def solve(str):
  first = ""
  second = ""
  for j in range(0, len(str)):
    if j%2 == 0:
      first += str[j]
    else:
      second += str[j]
  return first, second;

if __name__ == '__main__':
    T = int(input())
    Slist = []
    for i in range(0,T):
      Slist.append(input())

    for i in range(0, T):
      first, second = solve(Slist[i])
      print("{} {}".format(first,second))
