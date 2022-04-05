import uuid
import storage_manager
import projects_menu
from utils import input_utils, output_utils


auth_menu = {
    "1": "Register",
    "2": "Login"
}


def show_auth_menu():
    output_utils.print_menu(auth_menu, "Auth Menu")
    option = input_utils.get_numeric_input("Choose an option")

    while option not in auth_menu.keys():
        print("Choose a valid option")
        option = input_utils.get_numeric_input("Choose an option")

    if option == "1":
        register_new_user()
    elif option == "2":
        user = login_user()
        projects_menu.show_projects_menu(user)


def register_new_user():
    output_utils.print_header("Register new user")

    user_data = {
        "id": f"{uuid.uuid4()}",
        "first_name": input_utils.get_text_input("Enter your first name"),
        "last_name": input_utils.get_text_input("Enter your last name"),
        "email": input_utils.get_email_input("Enter your email"),
        "password": input_utils.get_mixed_input("Enter password")
    }

    while input_utils.get_mixed_input("Confirm password") != user_data["password"]:
        print("Password confirmation doesn't match password")

    storage_manager.store_user(user_data)

    output_utils.print_header("Successfully registered, you can login now")
    show_auth_menu()


def login_user():
    email = input_utils.get_email_input("Enter your email")
    user_data = storage_manager.get_user(email)
    while not user_data:
        print("This username doesn't exist")
        email = input_utils.get_email_input("Enter your email")
        user_data = storage_manager.get_user(email)

    while input_utils.get_mixed_input("Enter your password") != user_data["password"]:
        print("Password is wrong, try again!")

    return user_data
