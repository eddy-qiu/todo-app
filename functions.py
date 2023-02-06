FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Reads a text file and returns the list of to-do items"""
    with open(filepath, 'r') as file_local:
        return file_local.readlines()


def write_todos(todos_arg, filepath=FILEPATH):
    """Write todos onto a text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
