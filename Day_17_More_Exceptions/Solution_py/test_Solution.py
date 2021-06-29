import unittest
import Solution


class SolveTestCase(unittest.TestCase):
    def test_CaseI(self):
        n = 3
        p = 5
        excepted = 243
        myCalculator = Solution.Calculator()
        try:
            actual = myCalculator.power(n, p)
            self.assertEqual(excepted, actual)
        except:
            self.assertFail()

    def test_CaseII(self):
        n = 2
        p = 4
        excepted = 16
        myCalculator = Solution.Calculator()
        try:
            actual = myCalculator.power(n, p)
            self.assertEqual(excepted, actual)
        except:
            self.assertFail()

    def test_CaseIII(self):
        n = -1
        p = -2
        excepted = "n and p should be non-negative"
        myCalculator = Solution.Calculator()
        try:
            actual = myCalculator.power(n, p)
            self.assertFail()
        except Exception as e:
            self.assertEqual(excepted, str(e))

    def test_CaseIV(self):
        n = -1
        p = 3
        excepted = "n and p should be non-negative"
        myCalculator = Solution.Calculator()
        try:
            actual = myCalculator.power(n, p)
            self.assertFail()
        except Exception as e:
            self.assertEqual(excepted, str(e))
