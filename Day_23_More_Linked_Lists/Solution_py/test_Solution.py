import unittest
import Solution


class SolveTestCase (unittest.TestCase):
    def test_CaseI(self):
        mylist = Solution.Solution()
        T = [1, 2, 2, 3, 3, 4]
        head = None
        for i in T:
            data = i
            head = mylist.insert(head, data)
        head = mylist.removeDuplicates(head)
        expected = "1 2 3 4 "
        actual = mylist.displayForTest(head)
        self.assertEqual(actual, expected)
