#!/bin/python3

import math
import os
import random
import re
import sys

def reverse(arr):
    return " ".join(str(arr[i-1]) for i in range(len(arr), 0, -1))+ " "


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print (reverse(arr))
