import sys


class Solution:
    # Write your code here
    def __init__(self):
        self.queue = []
        self.stack = []

    def pushCharacter(self, ch):
        self.stack.append(ch)

    def popCharacter(self):
        return self.stack.pop()

    def enqueueCharacter(self, ch):
        self.queue.append(ch)

    def dequeueCharacter(self):
        return self.queue.pop(0)

    def printStack(self):
        return self.stack

    def printQueue(self):
        return self.queue


def forTest(s):
    # Create the Solution class object
    obj = Solution()

    l = len(s)
    # push/enqueue all the characters of string s to stack
    for i in range(l):
        obj.pushCharacter(s[i])
        obj.enqueueCharacter(s[i])

    isPalindrome = True
    '''
  pop the top character from stack
  dequeue the first character from queue
  compare both the characters
  '''
    for i in range(l // 2):
        if obj.popCharacter() != obj.dequeueCharacter():
            isPalindrome = False
            break
    # finally print whether string s is palindrome or not.
    if isPalindrome:
        return "The word, "+s+", is a palindrome."
    else:
        return "The word, "+s+", is not a palindrome."


if __name__ == "__main__":
    # read the string s
    s = input()
    print(forTest(s))
