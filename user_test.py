import unittest
from user import User


class TestUser(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """

    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = User('OwitiCharles', 'XyZ3thf1')

    def test_init(self):
        """
        Check if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username, 'OwitiCharles')
        self.assertEqual(self.new_user.password, 'XyZ3thf1')

    def test_save_user(self):
        """
        Check if a new user instance has been saved into the User list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


if __name__ == "__main__":
    unittest.main()
