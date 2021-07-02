#!/bin/python3

import math
import os
import random
import re
import sys


def BubbleSort(a):
    numSwaps = 0
    for i in range(0, len(a)):
        numberOfSwaps = 0
        for j in range(0, len(a)):
            if j + 1 < len(a):
                if a[j] > a[j + 1]:
                    temp = a[j]
                    a[j] = a[j + 1]
                    a[j + 1] = temp
                    numberOfSwaps += 1
                    numSwaps += 1
        if numberOfSwaps == 0:
            break
    first = a[0]
    last = a[-1]
    return numSwaps, first, last


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    numSwaps, first, last = BubbleSort(a)
    print('Array is sorted in {} swaps.'.format(numSwaps))
    print('First Element: {}'.format(first))
    print('Last Element: {}'.format(last))
