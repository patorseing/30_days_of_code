import unittest
import Solution

class SolveTestCase (unittest.TestCase):
  def test_CaseI (self):
    a = [1, 2, 3]
    numSwaps, first, last = Solution.BubbleSort(a)
    actual = [numSwaps, first, last]
    excepted = [0, 1, 3]
    self.assertEqual(excepted, actual)

  def test_CaseII (self):
    a = [3, 2, 1]
    numSwaps, first, last = Solution.BubbleSort(a)
    actual = [numSwaps, first, last]
    excepted = [3, 1, 3]
    self.assertEqual(excepted, actual)

  def test_CaseIII (self):
    a = [4, 3, 1, 2]
    numSwaps, first, last = Solution.BubbleSort(a)
    actual = [numSwaps, first, last]
    excepted = [5, 1, 4]
    self.assertEqual(excepted, actual)
