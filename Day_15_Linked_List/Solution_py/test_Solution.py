import unittest
import Solution

# python -m unittest


class SolveTestCase(unittest.TestCase):

    def test_SolveI(self):
        mylist = Solution.Solution()
        head = None
        for i in [2,3,4,1]:
            head = mylist.insert(head, i)
        self.assertEqual(mylist.displayForTest(head), "2 3 4 1 ")
