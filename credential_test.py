import unittest
from credential import Credentials


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

    def test_search_credential(self):
        """
        Check if credentials can be found by account name
        """
        self.new_credential.save_details()
        test_credential = Credentials("Twitter", "default-007", "asdfg")
        test_credential.save_details()
        the_credential = Credentials.search_credential("Twitter")
        self.assertEqual(the_credential.account, test_credential.account)

    def test_credential_exist(self):
        """
        check if we can return a true or false based on whether we find or can't find the credential.
        """
        self.new_credential.save_details()
        the_credential = Credentials("Twitter", "mikeycharles", "Mfh45hfk")
        the_credential.save_details()
        credential_is_found = Credentials.existing_credential("Twitter")
        self.assertTrue(credential_is_found)

    def test_display_all_saved_credentials(self):
        '''
        displays all the credentials that has been saved by the user
        '''

        self.assertEqual(Credentials.display_credentials(),
                         Credentials.credentials_list)


if __name__ == "__main__":
    unittest.main()
