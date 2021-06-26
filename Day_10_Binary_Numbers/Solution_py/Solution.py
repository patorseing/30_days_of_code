#!/bin/python3

import math
import os
import random
import re
import sys


def convertBinary(dec):
    bin = ""
    count = 0
    maxCount = 0
    while dec > 0:
        if dec % 2 == 0:
            if maxCount < count:
                maxCount = count
            count = 0
            bin += "0"
        else:
            count += 1
            bin += "1"
        dec >>= 1
    if maxCount < count:
        maxCount = count
    return maxCount


if __name__ == '__main__':
    n = int(input().strip())
    print(convertBinary(n))
