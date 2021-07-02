import unittest
import Solution


class SolveTestCase (unittest.TestCase):
    def test_CaseI(self):
        myTree = Solution.Solution()
        root = None
        T = [3, 5, 2, 1, 4, 6, 7]
        for i in T:
            data = i
            root = myTree.insert(root, data)
        height = myTree.getHeight(root)
        expected = 3
        self.assertEqual(height, expected)
