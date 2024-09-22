from pathlib import Path

"""
Provides a way to interact with the file system
in a more convenient way than dealing with os.path or the glob module.
Python 3.4+
"""


def get_folder_path(folder_name: str) -> Path:
    """
    Returns a Path object for the given folder name.
    """
    return Path(folder_name)


def build_complex_path(base_path: Path) -> Path:
    """
    Appends 'Default/AppData' to the given base path.
    """
    return base_path / "Default" / "AppData"


def print_absolute_path(path: Path) -> None:
    """
    Prints the absolute path of the given Path object.
    """
    print(path.resolve())


def enumerate_path_characters(path: Path) -> None:
    """
    Prints each character in the path string with its index.
    """
    for counter, entry in enumerate(str(path)):
        print(f"{counter}: {entry}")


def main() -> None:
    """
    Main function to demonstrate the usage of the above functions.
    """
    initial_path = Path("C:/Users")
    folder_path = get_folder_path(initial_path)
    print(folder_path)

    complex_path = build_complex_path(folder_path)
    print(complex_path)

    print_absolute_path(complex_path)
    enumerate_path_characters(complex_path)


if __name__ == "__main__":
    main()
