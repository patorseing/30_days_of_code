#!/bin/python3

import math
import os
import random
import re
import sys


def solve(N):
    result = ""
    if N % 2 == 1:
        result = "Weird"
    else:
        if N > 1 and N < 6:
            result = "Not Weird"
        elif N > 5 and N < 21:
            result = "Weird"
        else:
            result = "Not Weird"
    return result


if __name__ == '__main__':
    N = int(input())
    print(solve(N))
