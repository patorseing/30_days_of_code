import unittest
import Solution

# python -m unittest


class SolveTestCase(unittest.TestCase):

    def test_SolveI(self):
        i = "The Alchemist\nPaulo Coelho\n248"
        title = i.split('\n')[0]
        author = i.split('\n')[1]
        price = i.split('\n')[2]
        new_novel = Solution.MyBook(title, author, price)
        o = "Title: The Alchemist\nAuthor: Paulo Coelho\nPrice: 248"
        self.assertEqual(new_novel.displayForTest(), o)
