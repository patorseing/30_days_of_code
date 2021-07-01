import unittest
import Solution


class SolveTestCase(unittest.TestCase):

    def test_CaseI(self):
        n = 25
        my_calculator = Solution.Calculator()
        actual = my_calculator.divisorSum(n)
        excepted = 31
        self.assertEqual(actual, excepted)

    def test_CaseII(self):
        n = 20
        my_calculator = Solution.Calculator()
        actual = my_calculator.divisorSum(n)
        excepted = 42
        self.assertEqual(actual, excepted)

    def test_CaseIII(self):
        n = 6
        my_calculator = Solution.Calculator()
        actual = my_calculator.divisorSum(n)
        excepted = 12
        self.assertEqual(actual, excepted)
