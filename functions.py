FILEPATH = "todo.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of todos."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write te to do item in to the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
