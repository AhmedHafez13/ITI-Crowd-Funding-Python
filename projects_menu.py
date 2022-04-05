import uuid
import storage_manager
from utils import input_utils, output_utils

user_data = {}

projects_menu = {
    "1": "Create a new Project",
    "2": "View All Projects",
    "3": "Edit a Project",
    "4": "Delete a Project",
    "5": "Search for a Project"
}


def show_projects_menu(user=None):
    if user:
        global user_data
        user_data = user

    output_utils.print_menu(projects_menu, "Projects Menu")
    option = input_utils.get_numeric_input("Choose an option")

    while option not in projects_menu.keys():
        print("Choose a valid option")
        option = input_utils.get_numeric_input("Choose an option")

    if option == "1":
        create_project()
    elif option == "2":
        view_projects()
    elif option == "3":
        edit_project()
    elif option == "4":
        delete_project()
    elif option == "5":
        search_project()


def create_project():
    output_utils.print_header("Create a new project")

    project_data = {
        "id": f"{uuid.uuid4()}",
        "user_id": user_data["id"],
        "title": input_utils.get_text_input("Enter a title"),
        "details": input_utils.get_text_input("Enter the details"),
        "target": input_utils.get_numeric_input("Enter the total target"),
        "start_data": input_utils.get_date_input("Enter start data"),
        "end_data": input_utils.get_date_input("Enter end data")
    }

    storage_manager.store_project(project_data)

    output_utils.print_header("Successfully created")
    show_projects_menu()


def view_projects():
    projects = storage_manager.get_all_projects()
    output_utils.print_projects(projects)
    show_projects_menu()


def edit_project():
    projects = storage_manager.get_all_projects()

    own_projects = list(filter(
        lambda project: project["user_id"] == user_data["id"],
        projects
    ))

    if own_projects:
        output_utils.print_projects(own_projects)

        project_order = int(input_utils.get_numeric_input("Choose a project to edit"))
        target_project = own_projects[project_order-1]

        target_project["title"] = input_utils.get_text_input(
            f"Enter a new title, current title: {target_project['title']}"
        )
        target_project["details"] = input_utils.get_text_input(
            f"Enter a new details, current details: {target_project['details']}"
        )
        target_project["target"] = input_utils.get_numeric_input(
            f"Enter a new target, current target: {target_project['target']}"
        )
        target_project["start_data"] = input_utils.get_date_input(
            f"Enter a new start data, current start data: {target_project['start_data']}"
        )
        target_project["end_data"] = input_utils.get_date_input(
            f"Enter a new end data, current end data: {target_project['end_data']}"
        )

        storage_manager.update_projects(projects)

        output_utils.print_header("Successfully updated!")
        show_projects_menu()
    else:
        output_utils.print_header("Can't find any projects")


def delete_project():
    projects = storage_manager.get_all_projects()

    own_projects = list(filter(
        lambda project: project["user_id"] == user_data["id"],
        projects
    ))

    if own_projects:
        output_utils.print_projects(own_projects)

        project_order = int(input_utils.get_numeric_input("Choose a project to delete"))
        target_project = own_projects[project_order - 1]

        projects = list(filter(
            lambda project: project["id"] == target_project["id"],
            projects
        ))

        storage_manager.update_projects(projects)

        output_utils.print_header("Successfully deleted!")
        show_projects_menu()
    else:
        output_utils.print_header("Can't find any projects")


def search_project():
    pass
