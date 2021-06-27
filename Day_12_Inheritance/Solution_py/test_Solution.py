import unittest
import Solution

# python -m unittest


class SolveTestCase(unittest.TestCase):

    def test_SolveI(self):
        i = "Heraldo Memelli 8135627\n2\n100 80"
        firstName = i.split('\n')[0].split()[0]
        lastName = i.split('\n')[0].split()[1]
        idNum = i.split('\n')[0].split()[2]
        scores = list(map(int, i.split('\n')[2].split()))
        o = "Name: Memelli, Heraldo\nID: 8135627\nGrade: O"
        s = Solution.Student(firstName, lastName, idNum, scores)
        self.assertEqual(s.printPersonForTest()+"Grade: "+s.calculate(), o)
