#!/bin/python3

import math
import os
import random
import re
import sys

def solve (n,i):
  return "{} x {} = {}".format(n,i,n*i)

if __name__ == '__main__':
    n = int(input())
    for i in range(1,11):
      print(solve(n,i))
