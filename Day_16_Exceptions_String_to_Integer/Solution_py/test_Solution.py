#!/bin/python3

import unittest
import Solution


class SolveTestCase(unittest.TestCase):
    def test_SolveI(self):
        excepted = 3
        actual = Solution.parseInt("3")
        self.assertEqual(excepted, actual)

    def test_SolveII(self):
        excepted = "Bad String"
        actual = Solution.parseInt("za")
        self.assertEqual(excepted, actual)
