import unittest
import Solution


class ConcatTestCase(unittest.TestCase):

     def test_SolveI(self):
        first, second = Solution.solve("Hacker")
        self.assertEqual(first+" "+second, "Hce akr")

     def test_SolveII(self):
        first, second = Solution.solve("Rank")
        self.assertEqual(first+" "+second, "Rn ak")
