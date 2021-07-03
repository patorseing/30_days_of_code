import unittest
import Solution

class SolveTestCase(unittest.TestCase):
  def test_CaseI(self):
    actual = Solution.CalculateFin([9,6, 2015], [6, 6, 2015])
    excepted = 45
    self.assertEqual(actual, excepted)

  def test_CaseII(self):
    actual = Solution.CalculateFin([31, 12, 2009], [1, 1, 2010])
    excepted = 0
    self.assertEqual(actual, excepted)

  def test_CaseIII(self):
    actual = Solution.CalculateFin([1, 1, 2010], [31, 12, 2009])
    excepted = 10000
    self.assertEqual(actual, excepted)
