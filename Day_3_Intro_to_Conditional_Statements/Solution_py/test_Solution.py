import unittest
import Solution


class ConcatTestCase(unittest.TestCase):

     def test_Weird(self):
        result = Solution.solve(3)
        self.assertEqual(result, "Weird")

     def test_Not_Weird(self):
        result = Solution.solve(24)
        self.assertEqual(result, "Not Weird")
