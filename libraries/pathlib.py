from pathlib import Path

"""
Provides a way to interact with file system in a more convenient way than dealing with os.path or the glob module.
Python 3.4+
"""


def return_folder(folder_name):
    path = Path(folder_name)
    print(path)
    return path


def return_complex_path(path):
    path = path / 'Default' / 'AppData'
    print(path)
    return path


def print_absolute_path():
    print(path.resolve())


def enumerate_path_characters(path):
    for counter, entry in enumerate(str(path)):
        print(f"{counter}: {entry}")

if __name__ == "__main__":
    path = "C:\\Users"
    path = return_folder(path)
    path = return_complex_path(path)
    print_absolute_path()
    enumerate_path_characters(path)
