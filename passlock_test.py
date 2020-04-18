import unittest
from passlock import User


class TestClass(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """

    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = User('default-007', "qwerty")

    def test_init(self):
        """
        test case to chek if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username, 'default-007')
        self.assertEqual(self.new_user.password, 'qwerty')


if __name__ == "___main__":
    unittest.main()
