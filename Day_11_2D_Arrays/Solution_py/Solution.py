#!/bin/python3

import math
import os
import random
import re
import sys


def calHourGlass(Arr2D):
    # print(Arr2D)
    resultList = []
    count = 1
    for j in range(0, len(Arr2D[0])):
        for i in range(0, len(Arr2D[1])):
            result = 0
            if i+1 < len(Arr2D[0]) and i+2 < len(Arr2D[0]) and j+1 < len(Arr2D[1]) and j+2 < len(Arr2D[1]):
                one = Arr2D[i][j]
                two = Arr2D[i][j+1]
                three = Arr2D[i][j+2]
                four = Arr2D[i+1][j+1]
                five = Arr2D[i+2][j]
                six = Arr2D[i+2][j+1]
                seven = Arr2D[i+2][j+2]
                # print("#{}: {} {} {}\n      {}  \n    {} {} {}".format(
                #     count, one, two, three, four, five, six, seven))
                result = one + two + three + four + five + six + seven
                resultList.append(result)
                count += 1
    return max(resultList)


if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(calHourGlass(arr))
