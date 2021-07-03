#!/bin/python3

import math
import os
import random
import re
import sys


class Database:
    def __init__(self):
        self.emailprofile = []

    def sortFName(self,profile):
        return profile['firstName']

    def addEmail(self, fname, email):
        if re.search(".+@gmail\.com$", email):
            self.emailprofile.append({'firstName': fname, 'emailID': email})
            self.emailprofile.sort(key=self.sortFName)

    def printFname(self):
        res = ""
        for i in range(len(self.emailprofile)):
            res += self.emailprofile[i]['firstName']
            if i+1 != len(self.emailprofile):
                res += "\n"
        return res


if __name__ == '__main__':
    N = int(input().strip())

    db = Database()
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        db.addEmail(firstName, emailID)
    print(db.printFname())
