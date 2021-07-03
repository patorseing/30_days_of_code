import unittest
import Solution


class SolveTestCase(unittest.TestCase):
    def test_CaseI(self):
        excepted = 1
        actual = Solution.bitwiseAnd(5, 2)
        self.assertEqual(excepted, actual)

    def test_CaseII(self):
        excepted = 4
        actual = Solution.bitwiseAnd(8, 5)
        self.assertEqual(excepted, actual)

    def test_CaseIII(self):
        excepted = 0
        actual = Solution.bitwiseAnd(2, 2)
        self.assertEqual(excepted, actual)
