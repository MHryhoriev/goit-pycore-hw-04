def get_cats_info(path: str) -> list[dict]:
    """
    Load and return a list of dictionaries containing cat information from a file.

    Args:
    - path (str): The path to the file containing cat data.

    Returns:
    - list[dict]: A list of dictionaries, each representing a cat's information with keys 'id', 'name', and 'age'.

    Raises:
    - FileNotFoundError: If the specified file is not found.
    - IOError: If there is an error opening or reading data from the file.
    """

    cats_data = read_cats_data(path)
    cats_info = parse_cats_data(cats_data)
    return cats_info

def read_cats_data(path: str) -> list[str]:
    """
    Read cat data from a file and return it as a list of strings.

    Args:
    - path (str): The path to the file containing cat data.

    Returns:
    - list[str]: A list of strings, each representing a line of cat data from the file.

    Raises:
    - FileNotFoundError: If the specified file is not found.
    - IOError: If there is an error opening or reading data from the file.
    """

    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File '{path}' not found!")
    except IOError as exeption:
        print(f"IOError: {exeption}")

    return []

def parse_cats_data(cats_data: list[str]) -> list[dict]:
    """
    Parse cat data from a list of strings into a list of dictionaries.

    Args:
    - cats_data (list[str]): A list of strings, each representing a line of cat data in the format "id, name, age".

    Returns:
    - list[dict]: A list of dictionaries, each representing a cat's information with keys 'id', 'name', and 'age'.
    """

    cats_info = []
    for item in cats_data:
        parts = item.strip().split(",")
        if len(parts) == 3:
            cat_info = {
                "id": parts[0].strip(),
                "name": parts[1].strip(),
                "age": parts[2].strip()
            }
            cats_info.append(cat_info)
    return cats_info
