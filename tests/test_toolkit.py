import unittest

from toolkit.csv_processor import read_csv
from toolkit.data_validator import validate_user
from toolkit.exceptions import InvalidUserError


class TestCSVProcessor(unittest.TestCase):

    def test_read_csv(self):
        users = read_csv("sample_data/users.csv")

        self.assertEqual(len(users), 4)
        self.assertEqual(users[0]["name"], "Koti")


class TestUserValidation(unittest.TestCase):

    def test_valid_user(self):
        user = {
            "name": "Koti",
            "email": "koti@gmail.com",
            "age": 31
        }

        self.assertTrue(validate_user(user))

    def test_missing_name(self):
        user = {
            "name": "",
            "email": "koti@gmail.com",
            "age": 31
        }

        with self.assertRaises(InvalidUserError):
            validate_user(user)

    def test_underage_user(self):
        user = {
            "name": "Test",
            "email": "test@gmail.com",
            "age": 15
        }

        with self.assertRaises(InvalidUserError):
            validate_user(user)


if __name__ == "__main__":
    unittest.main()
    