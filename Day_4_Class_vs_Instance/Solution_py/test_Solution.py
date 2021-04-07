import unittest
import Solution


class ConcatTestCase(unittest.TestCase):

    def test_caseI(self):
        age = -1
        p = Solution.Person(age)
        result = p.amIOldLogic()
        self.assertEqual(result, "You are young.")
        for j in range(0, 3):
            p.yearPasses()
        result = p.amIOldLogic()
        self.assertEqual(result, "You are young.")

    def test_caseII(self):
        age = 10
        p = Solution.Person(age)
        result = p.amIOldLogic()
        self.assertEqual(result, "You are young.")
        for j in range(0, 3):
            p.yearPasses()
        result = p.amIOldLogic()
        self.assertEqual(result, "You are a teenager.")

    def test_caseIII(self):
        age = 16
        p = Solution.Person(age)
        result = p.amIOldLogic()
        self.assertEqual(result, "You are a teenager.")
        for j in range(0, 3):
            p.yearPasses()
        result = p.amIOldLogic()
        self.assertEqual(result, "You are old.")

    def test_caseIV(self):
        age = 18
        p = Solution.Person(age)
        result = p.amIOldLogic()
        self.assertEqual(result, "You are old.")
        for j in range(0, 3):
            p.yearPasses()
        result = p.amIOldLogic()
        self.assertEqual(result, "You are old.")
