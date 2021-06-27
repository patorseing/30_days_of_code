import unittest
import Solution

# python -m unittest


class SolveTestCase(unittest.TestCase):

    def test_SolveI(self):
        i = [1, 2, 5]
        d = Solution.Difference(i)
        d.computeDifference()
        o = 4
        self.assertEqual(d.maximumDifference, o)

    def test_SolveII(self):
        i = [8, 19, 3, 2, 7]
        d = Solution.Difference(i)
        d.computeDifference()
        o = 17
        self.assertEqual(d.maximumDifference, o)

    def test_SolveIII(self):
        i = [8, 8, 8, 8, 8]
        d = Solution.Difference(i)
        d.computeDifference()
        o = 0
        self.assertEqual(d.maximumDifference, o)
