import sys
from colorama import Fore, Style
from pathlib import Path

def validate_input_path():
    """
    Validate command line arguments and directory path.

    Returns:
    - directory_path (Path): Path object representing the directory to list.
    """
    if len(sys.argv) != 2:
        print(f"{Fore.RED} [ERROR] Usage: py main.py /path/to/your/directories")
        print(Style.RESET_ALL)
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    if not directory_path.exists() or not directory_path.is_dir():
        print(f"{Fore.RED} [ERROR] Directory '{directory_path}' not found or is not a valid directory!")
        print(Style.RESET_ALL)
        sys.exit(1)

    return directory_path


def list_files_and_directories(directory_path: Path, depth: int = 0):
    """
    List all files and directories recursively starting from a given directory.

    Args:
    - directory_path (Path): Path object representing the directory to list.
    - depth (int, optional): Current depth of recursion (default is 0).

    Returns:
    - None
    """

    if depth == 0:
        print(f"{Fore.BLUE} {directory_path.name}/{Style.RESET_ALL}")

    for path in directory_path.iterdir():
        indent = '  ' * (depth + 1)
        if path.is_file():
            print(f"{indent}{Fore.GREEN} {path.name}{Style.RESET_ALL}")
        elif path.is_dir():
            print(f"{indent}{Fore.BLUE} {path.name}/")
            list_files_and_directories(path, depth + 1)