import unittest
import Solution


class ConcatTestCase(unittest.TestCase):

     def test_SolveI(self):
        result = Solution.solve(2,1)
        self.assertEqual(result, "2 x 1 = 2")

     def test_SolveI(self):
        result = Solution.solve(2,2)
        self.assertEqual(result, "2 x 2 = 4")
