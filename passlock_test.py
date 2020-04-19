import unittest
from passlock import User
from passlock import Credentials


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


class TestCredentials(unittest.TestCase):
    """
    Test class for Credentials class
    """

    def setUp(self):
        """
        Method that runs before individual credential test are run
        """
        self.new_credential = Credentials('Gmail', 'default-007', 'qwerty')

    def test_init(self):
        """
        Test Case to check if new Credentials are initialised correctly.
        """
        self.assertEqual(self.new_credential.account, "Gmail")
        self.assertEqual(self.new_credential.userName, "default-007")
        self.assertEqual(self.new_credential.password, "qwerty")

    def test_save_credential(self):
        """
        Test if credential list has been saved into list
        """
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def tearDown(self):
        """
        Clean up after each test case
        """
        Credentials.credentials_list = []

    def test_multiple_account(self):
        """
        Test if multiple accounts can be saved
        """
        self.new_credential.save_details()
        test_credential = Credentials("Twitter", "default-007", "asdfg")
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credential(self):
        """
        Test if account credentials can be removed
        """
        self.new_credential.save_details()
        test_credential = Credentials("Twitter", "default-007", "asdfg")
        test_credential.save_details()
        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)


if __name__ == "__main__":
    unittest.main()
