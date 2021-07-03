import unittest
import Solution

class SolveTestCase(unittest.TestCase):
  def test_CaseI(self):
    i = 12
    actual = Solution.isPrime(i)
    excepted = "Not prime"
    self.assertEqual(actual, excepted)

  def test_CaseII(self):
    i = 5
    actual = Solution.isPrime(i)
    excepted = "Prime"
    self.assertEqual(actual, excepted)

  def test_CaseIII(self):
    i = 7
    actual = Solution.isPrime(i)
    excepted = "Prime"
    self.assertEqual(actual, excepted)

  def test_CaseIV(self):
    i = 1
    actual = Solution.isPrime(i)
    excepted = "Not prime"
    self.assertEqual(actual, excepted)

  def test_CaseV(self):
    i = 2
    actual = Solution.isPrime(i)
    excepted = "Prime"
    self.assertEqual(actual, excepted)
