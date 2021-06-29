import unittest
import Solution


class SolveTestCase(unittest.TestCase):

    def test_CaseStack(self):
        obj = Solution.Solution()
        word_test = "yes"
        # word_test = "racecar"

        l = len(word_test)
      # push/enqueue all the characters of string s to stack
        for i in range(l):
            obj.pushCharacter(word_test[i])
        excepted = ['y', 'e']
        print('test_CaseStack', end="")
        print(obj.printStack(), end="")
        obj.popCharacter()
        actual = obj.printStack()
        print(obj.printStack())
        self.assertEqual(excepted, actual)

    def test_CaseQueue(self):
        obj = Solution.Solution()
        word_test = "yes"

        l = len(word_test)
        # push/enqueue all the characters of string s to stack
        for i in range(l):
            obj.enqueueCharacter(word_test[i])
        excepted = ['e', 's']
        print('test_CaseQueue', end="")
        print(obj.printQueue(), end="")
        obj.dequeueCharacter()
        actual = obj.printQueue()
        print(obj.printQueue())
        self.assertEqual(excepted, actual)

    def test_CaseI(self):
        excepted = "The word, racecar, is a palindrome."
        actual = Solution.forTest("racecar")
        self.assertEqual(excepted, actual)

    def test_CaseII(self):
        excepted = "The word, yes, is not a palindrome."
        actual = Solution.forTest("yes")
        self.assertEqual(excepted, actual)
