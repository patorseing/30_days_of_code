import unittest
import Solution

# python -m unittest
class SolveTestCase(unittest.TestCase):

     def test_SolveI(self):
        result = Solution.convertBinary(5)
        self.assertEqual(result, 1)

     def test_SolveII(self):
        result = Solution.convertBinary(13)
        self.assertEqual(result, 2)
