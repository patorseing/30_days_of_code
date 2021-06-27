#!/bin/python3

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPersonForTest(self):
        return "Name: {}, {}\nID: {}\n".format(self.lastName,  self.firstName, self.idNumber)

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
    # body of the constructor`
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

    def calculate(self):
        raw = sum(self.scores)/len(self.scores)
        if raw < 40:
            return "T"
        elif (40 <= raw) and (raw < 55):
            return "D"
        elif (55 <= raw) and (raw < 70):
            return "P"
        elif (70 <= raw) and (raw < 80):
            return "A"
        elif (80 <= raw) and (raw < 90):
            return "E"
        elif (90 <= raw) and (raw <= 100):
            return "O"
        else:
            return ""


if __name__ == '__main__':
    line = input().split()
    firstName = line[0]
    lastName = line[1]
    idNum = line[2]
    numScores = int(input())  # not needed for Python
    scores = list(map(int, input().split()))
    s = Student(firstName, lastName, idNum, scores)
    s.printPerson()
    print("Grade:", s.calculate())
