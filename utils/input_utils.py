import utils.validation_utils as validation_utils


def get_numeric_input(message):
    user_input = input("> " + message + ":\n")
    while not user_input.isdigit():
        print("Your input is invalid")
        user_input = input("> " + message + ":\n")
    return user_input


def get_text_input(message):
    user_input = input("> " + message + ":\n")
    while not user_input:
        print("Your input is invalid")
        user_input = input("> " + message + ":\n")
    return user_input


def get_mixed_input(message):
    user_input = input("> " + message + ":\n")
    while not user_input:
        print("Your input is invalid")
        user_input = input("> " + message + ":\n")
    return user_input


def get_email_input(message):
    user_input = input("> " + message + ":\n")
    while not validation_utils.is_valid_email(user_input):
        print("Your input is invalid email")
        user_input = input("> " + message + ":\n")
    return user_input


def get_date_input(message):
    user_input = input("> " + message + ":\n")
    while not validation_utils.is_valid_date(user_input):
        print("Your input is invalid date")
        user_input = input("> " + message + ":\n")
    return user_input
