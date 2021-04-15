# Enter your code here. Read input from STDIN. Print output to STDOUT

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    T = int(input())
    Slist = []
    for i in range(0,T):
      Slist.append(input())

    for i in range(0, T):
      first = ""
      second = ""
      for j in range(0, len(Slist[i])):
        if j%2 == 0:
          first += Slist[i][j]
        else:
          second += Slist[i][j]
      print("{} {}".format(first,second))
