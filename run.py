from user import User
from credential import Credentials


def create_new_user(username, password):
    """
    Create new User with username and password
    """
    new_user = User(username, password)
    return new_user


def save_user(user):
    """
    Function to save a new user
    """
    user.save_user()


def display_user():
    """
    Display user
    """
    return User.display_user()


def login_user(username, password):
    """
    Check if uesr exist and login the user
    """
    check_user = Credentials.verify_user(username, password)
    return check_user


def create_new_credential(account, userName, password):
    """
    Create new user credentials for a user
    """
    new_credential = Credentials(account, userName, password)
    return new_credential


def save_credentials(credentials):
    """
    Save credentials to list
    """
    credentials.save_details()


def display_accounts_details():
    """
    returns all the saved credential.
    """
    return Credentials.display_credentials()


def delete_credential(credentials):
    """
    delete a Credentials from credentials list
    """
    credentials.delete_credentials()


def search_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.search_credential(account)


def check_credentials(account):
    """
    Function that check if a Credentials exists with that account name and return true or false
    """
    return Credentials.existing_credential(account)


def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password = Credentials.generatePassword()
    return auto_password


def copy_password(account):
    """
    A funct that copies the password using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    return Credentials.copy_password(account)


def main():
    print("Hello Welcome to the PassLocker...\n Please enter one of the following to proceed.\n NA ---  New Account  \n EA ---  Existing Account  \n")
    code = input("").lower().strip()
    if code == "na":
        print("Sign Up")
        print('*' * 50)
        username = input("User_name: ")
        while True:
            print(" TP - Type pasword:\n GP - Generate random Password")
            password_Choice = input().lower().strip()
            if password_Choice == 'tp':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                password = generate_Password()
                break
            else:
                print("Invalid password please try again")
        save_user(create_new_user(username, password))
        print("*"*85)
        print(
            f"Hello {username}, Your account has been created succesfully! Your password is: {password}")
        print("*"*85)
    elif code == "ea":
        print("*"*50)
        print("Enter your User name and your Password to log in:")
        print('*' * 50)
        username = input("User_name: ")
        password = input("password: ")
        login = login_user(username, password)
        if login_user == login:
            print(f"Hello {username}.Welcome To PassLocker")
            print('\n')
    while True:
        print("Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")
        code = input().lower().strip()
        if code == "cc":
            print("Create New Credential")
            print("."*20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(
                    " TP - To type your own pasword if you already have an account:\n GP - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice == 'gp':
                    password = generate_Password()
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_new_credential(
                account, userName, password))
            print('\n')
            print(
                f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully")
            print('\n')
        elif code == "dc":
            if display_accounts_details():
                print("Here's your list of acoounts: ")

                print('*' * 30)
                print('_' * 30)
                for account in display_accounts_details():
                    print(
                        f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('_' * 30)
                print('*' * 30)
            else:
                print("You don't have any credentials saved yet..........")
        elif code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if search_credential(search_name):
                find_credential = search_credential(search_name)
                print(f"Account Name : {find_credential.account}")
                print('-' * 50)
                print(
                    f"User Name: {find_credential.userName} Password :{find_credential.password}")
                print('-' * 50)
            else:
                print("That Credential does not exist")
                print('\n')
        elif code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if search_credential(search_name):
                find_credential = search_credential(search_name)
                print("_"*50)
                find_credential.delete_credentials()
                print('\n')
                print(
                    f"Your stored credentials for : {find_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print(
                    "That Credential you want to delete does not exist in your store yet")

        elif code == 'gp':

            password = generate_Password()
            print(
                f" {password} Has been generated succesfull. You can proceed to use it to your account")
        elif code == 'ex':
            print("Thanks for using passwords store manager.. See you next time!")
            break
        else:
            print(
                "Wrong entry... Check your entry again and let it match those in the menu")
    else:
        print("Please enter a valid input to continue")


if __name__ == '__main__':
    main()
