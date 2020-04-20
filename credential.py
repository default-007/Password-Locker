import random
import string
import pyperclip
from user import User


class Credentials():
    """
    Create a new Credentials class to create new objects
    """

    credentials_list = []

    def __init__(self, account, userName, password):
        """
        Method to define credentials to be stored
        """
        self.account = account
        self.userName = userName
        self.password = password

    @classmethod
    def verify_user(cls, username, password):
        """
        Method to verify if in the user_list
        """
        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                a_user == user.username
        return a_user

    def save_details(self):
        """
        Save new credentials in the credentials list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        Delete credentials in the credentilas list
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def search_credential(cls, account):
        """
        Checks if account.name and return credentials matching the account
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential

    @classmethod
    def existing_credential(cls, account):
        """
        Check if credential exist and return true or false
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False

    @classmethod
    def copy_password(cls, account):
        """
        Copy password of account found
        """
        logged_credential = Credentials.search_credential(account)
        pyperclip.copy(logged_credential.password)

    def generate_password(stringLength=10):
        """
        Generate random password with letters and numbers
        """
        password = string.ascii_uppercase+string.ascii_lowercase+string.digits
        return ''.join(random.choice(password)for i in range(stringLength))
