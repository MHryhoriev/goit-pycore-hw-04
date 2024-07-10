def total_salary(path: str) -> tuple:
    """
    Calculate total salary sum and average from a file.

    Args:
    - path (str): The path to the file containing salary data.

    Returns:
    - tuple: A tuple containing total salary sum and average salary.
    """

    salary_data = load_salary_data(path)
    if salary_data:
        stats = calculate_salary_statistics(salary_data)
        return stats
    
    return (0, 0)
    
def load_salary_data(path: str) -> list[int]:
    """
    Load salary data from a file.

    Args:
    - path (str): The path to the file containing salary data.

    Returns:
    - list[int]: A list of integers representing salaries.
    """

    salaries = []
    line_number = 0
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line_number += 1
                parts = line.strip().split(",")
                if len(parts) == 2:
                    salaries = convert_salaries(salaries, parts, line_number)
        return salaries
    except FileNotFoundError:
        print(f"File '{path}' not found!")
    except IOError as exception:
        print(f"IOError: {exception}")

    return []

def convert_salaries(salaries: list, parts: list, line_number: int) -> list:
    """
    Convert salary data from string format to integers.

    Args:
    - salaries (list): The current list of salaries.
    - parts (list): Parts of a line split by comma (name, salary).
    - line_number (int): The current line number in the file.

    Returns:
    - list: Updated list of salaries.
    """

    try:
        salary = int(parts[1].strip())
        salaries.append(salary)
    except ValueError:
        print(f"Number conversion error on line {line_number}: {parts[1]}")

    return salaries

def calculate_salary_statistics(salaries: list) -> tuple:
    """
    Calculate total sum and average salary from a list of salaries.

    Args:
    - salaries (list): A list of integers representing salaries.

    Returns:
    - tuple: A tuple containing total sum of salaries and average salary.
    """

    if not salaries:
        return (0, 0)
    
    total_sum = sum(salaries)
    count = len(salaries)
    average_salary = total_sum // count

    return (total_sum, average_salary)