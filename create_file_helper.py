import os


def create_py_file(problem_title):
    name = problem_title
    name = name.lower().replace(" ", "_").replace(".", "")
    print(name)

    current_working_directory = os.getcwd()
    print(f"The current working directory is: {current_working_directory}")

    file_name = os.path.join(current_working_directory, f"{name}.py")
    content = "from typing import List\n\n\n"

    with open(file_name, 'w') as file:
        file.write(content)


create_py_file(
    "70. Climbing Stairs"
)
