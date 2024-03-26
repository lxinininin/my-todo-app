FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


# if we run this script (function.py), the "__name__" variable is "__main__"
# and if we run the cli.py (which has already imported this file),
# the "__name__" variable is "functions" (the name of this script)
# this can be used to identify who runs the code
print(__name__)
if __name__ == "__main__":
    # so if we run this script directly, the content below will show
    print("Hello")
    print(get_todos())