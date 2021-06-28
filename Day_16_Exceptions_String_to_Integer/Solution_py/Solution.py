#!/bin/python3

import math
import os
import random
import re
import sys


def parseInt(n):
    out = ""
    try:
        out = int(n)
    except ValueError:
        out = "Bad String"
    return out


if __name__ == '__main__':
    S = input()
    print(parseInt(S))


# import sys

# def parseInt(n):
#     out = ""
#     try:
#         out = int(n)
#     except ValueError:
#         out = "Bad String"
#     return out

# S = input()
# print(parseInt(S))
