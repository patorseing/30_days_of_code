import unittest
import Solution


class TestCase(unittest.TestCase):
    def test_solve_found(self):
        phone_book = {
            "sam": 99912222,
            "tom": 11122222,
            "harry": 12299933,
        }
        result = Solution.search_phone_book(phone_book, "sam")
        self.assertEqual(result, "sam=99912222")

    def test_solve_not_found(self):
        phone_book = {
            "sam": 99912222,
            "tom": 11122222,
            "harry": 12299933,
        }
        result = Solution.search_phone_book(phone_book, "edward")
        self.assertEqual(result, "Not found")
