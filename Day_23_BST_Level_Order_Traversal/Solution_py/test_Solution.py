import unittest
import Solution


class SolveTestCase(unittest.TestCase):
    def test_CaseI(self):
        T = [3, 5, 4, 7, 2, 1]
        myTree = Solution.Solution()
        root = None
        for i in T:
          data = i
          root = myTree.insert(root, data)
        self.assertEqual(myTree.levelOrderForTest(root), "3 2 5 1 4 7 ")
