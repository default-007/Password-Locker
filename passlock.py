import string
import pyperclip


class User:

    """
    Create User class that gnerates new instances for uer.
    """

    user_list = []

    def __init__(self, username, password):
        """
        Method taht defines the properties of a user
        """
        self.username = username
        self.password = password

    def save_user(self):
        """
        Method to save a new user into the user list
        """
        User.user_list.append(self)
