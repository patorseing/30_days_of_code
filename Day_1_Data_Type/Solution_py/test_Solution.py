import unittest
import Solution


class ConcatTestCase(unittest.TestCase):

     def test_plusInt(self):
        result = Solution.plusInt(12)
        self.assertEqual(result, 16)
     def test_plusFloat(self):
        result = Solution.plusInt(4.0)
        self.assertEqual(result, 8.0)

     def test_concat(self):
        result = Solution.concat(
            "is the best place to learn and practice coding!")
        self.assertEqual(
            result, "HackerRank is the best place to learn and practice coding!")
