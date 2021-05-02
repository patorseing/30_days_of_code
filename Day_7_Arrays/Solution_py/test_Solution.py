import unittest
import Solution


class ConcatTestCase(unittest.TestCase):

     def test_SolveI(self):
        result = Solution.reverse([1,4,3,2])
        self.assertEqual(result, "2 3 4 1 ")
