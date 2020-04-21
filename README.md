# Password-Locker

## Author

[Brian Otieno](https://github.com/default-007)

## Description

A python application that manages login and signup credentials of a person for various accounts i.e. username and passwords for each account. It also stores the passwords and generates a unique password for a user if they do not want to generate new passwords by themselves.

## Problem

- User create an account for the application or log into the application.
- Store my existing acounts login details for various accounts that i have registered for.
- Generate new password for an account that i haven't registered for and store it with the account name.
- Delete stored account login details that i do now want anymore.
- Copy my credentials to the clipboard

## Installation / Setup instruction

### The application requires the following installations to operate

- python3.6
- pyperclip
- pip

#### Cloning

- Open Terminal {Ctrl+Alt+T}

- git clone `https://github.com/default-007/Password-Locker.git`

- cd Password-Locker

- code . or atom . based on the text editor you have.

### Running the Application

- To run the application, open the cloned file in terminal and run the following commands:

        python3 run.py

## BDD

| Behaviour                                                 |                        Input                        |                                                                                                                                               Output |
| :-------------------------------------------------------- | :-------------------------------------------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------: |
| Open the application on the terminal                      |         Run the command `$ python3 run.py`          |                                                                       Welcome to your PassLocker Store... NA --- New Account EA --- Existing Account |
| Select NA                                                 |             input username and password             |                                                                          Hello `username`, Account created succesfully! Your password is: `password` |
| Select EA                                                 | Enter your password and username you signed up with |                                                                                      Abbreviations menu to help you navigate through the application |
| Store a new credential in the application                 |                     Enter `CC`                      |                      Enter Account, username, password choose `tp` to enter your password or `gp` for the application to generate a password for you |
| Display all stored credentials                            |                     Enter `DC`                      |                                                         A list of all credentials that has been stored or `You don't have any credentials saved yet` |
| Find a stored credential based on account name            |                     Enter `FC`                      |                                                                        Enter the Account Name you want to search for and returns the account details |
| Delete an existing credential that you don't want anymore |                      Enter `D`                      | Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exixt |
| Exit the application                                      |                     Enter `EX`                      |                                                                                                                                The application exits |

## Technologies Used

- python3.6

## Known Bugs

- There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information

If you have any question or contributions, please email me at [brianokola@@gmail.com]

## License

- _MIT License:_
- Copyright (c) 2020 **Brian Otieno**
