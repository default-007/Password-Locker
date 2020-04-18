import string
import pyperclip


class User:

    """
    Create User class that gnerates new instances for uer.
    """

    def __init__(self, username, password):
        """
        Method taht defines the properties of a user
        """
        self.username = username
        self.password = password
