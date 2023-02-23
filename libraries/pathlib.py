from pathlib import Path

"""
Provides a way to interact with file system
in a more convenient way than dealing with os.path or the glob module.
Python 3.4+
"""


def return_folder_path(folder_name: str) -> Path:
    folder_path = Path(folder_name)
    return folder_path


def return_complex_path(path):
    path = path / "Default" / "AppData"
    return path


def print_absolute_path(path):
    print(path.resolve())


def enumerate_path_characters(path):
    for counter, entry in enumerate(str(path)):
        print(f"{counter}: {entry}")


def main():
    initial_path = "C:\\Users"
    folder_path = return_folder_path(initial_path)
    print(folder_path)
    complex_path = return_complex_path(folder_path)
    print(complex_path)
    print_absolute_path(complex_path)
    enumerate_path_characters(complex_path)


if __name__ == "__main__":
    main()
