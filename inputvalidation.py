"""This file handles input.

It ensures that no errors and invalid input is
entered, if it is, it asks the user to try again.
"""
import time
import os


def check_input(message, variety, error_message):
    """Get then validate input.

    This function gets user input, validates it,
    and then returns it.

    Parameters:
        message (str): Message displayed when asking
        for input.
        variaty (data type): Type of data accepted as input.
        error_message (str): Message displayed when invalid
        input is entered.

    Returns:
        user_choice (type is variable): Specific user input based on
        parameters.
    """
    while True:
        try:
            user_choice = variety(input(message))
            return user_choice
        except:
            os.system("clear")
            print(error_message)


def pos_int(message, error_message):
    """Get then validate integer input.

    This functions gets a positive integer
    from the user as input, validates it,
    and then returns it.

    Parameters:
        message (str): Message displayed when asking
        for input.
        error_message (str): Message displayed when invalid
        input is entered.

    Returns:
        user_choice (int): Specific user input based on
        parameters.
    """
    while True:
        try:
            user_choice = int(input(message))
            if user_choice < 0:
                os.system("clear")
                print(error_message)
                time.sleep(1)
                continue
            else:
                return user_choice
        except:
            os.system("clear")
            print(error_message)
            time.sleep(1)
