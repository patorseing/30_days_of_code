#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    arr = " ".join(str(arr[i-1]) for i in range(len(arr), 0, -1))
    print (arr)
