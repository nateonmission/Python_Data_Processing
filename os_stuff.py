from os import system, name
import os


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def clear_old_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        pass
