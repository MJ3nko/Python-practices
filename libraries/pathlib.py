from pathlib import Path

"""
Provides a way to interact with file system in a more convenient way than dealing with os.path or the glob module.
Python 3.4+
"""


def print_folder(folder_name):
    path = Path(folder_name)
    print(path)
    return path


def print_complex_path(path):
    path = path / 'Default' / 'AppData'
    print(path)
    return path


def print_absolute_path():
    print(path.resolve())


if __name__ == "__main__":
    path = "C:\\Users"
    path = print_folder(path)
    path = print_complex_path(path)
    path = print_absolute_path()
