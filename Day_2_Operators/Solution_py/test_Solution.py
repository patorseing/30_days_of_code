import unittest
import Solution


class ConcatTestCase(unittest.TestCase):

     def test_solve(self):
        result = Solution.solve(12.00, 20, 8)
        self.assertEqual(result, 15)
