import unittest
import Solution


class SolveTestCase(unittest.TestCase):
    def test_caseI(self):
        N = [
            "riya riya@gmail.com",
            "julia julia@julia.me",
            "julia sjulia@gmail.com",
            "julia julia@gmail.com",
            "samantha samantha@gmail.com",
            "tanya tanya@gmail.com"
        ]

        db = Solution.Database()

        for N_itr in N:
            first_multiple_input = N_itr.split()

            firstName = first_multiple_input[0]

            emailID = first_multiple_input[1]
            db.addEmail(firstName, emailID)
        actual = db.printFname()
        excepted = "julia\njulia\nriya\nsamantha\ntanya"
        self.assertEqual(actual, excepted)
