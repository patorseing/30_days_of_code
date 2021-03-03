import unittest
from Solution import concat

class ConcatTestCase(unittest.TestCase):

  def test_concat(self):
       result = concat("Welcome to 30 Days of Code!")
       self.assertEqual(result, "Hello, World. \nWelcome to 30 Days of Code!")

  def test_concatF(self):
       result = concat("Welcome to 30 Days of Code!")
       self.assertEqual(result, False)
