import numpy as np


def get_csv_column_name(filename) -> np.ndarray:
    """
    Extracts the column names from a CSV file.

    Args:
        filename (str): The path to the CSV file.

    Returns:
        np.ndarray: An array of column names extracted from the CSV file.
    """
    with open(filename, 'r') as f:
        headline = f.readline()
        names = [name.strip() for name in headline.split(',')]

        return np.array(names)


def get_name2idx_map(lst: list):
    """
    Generate a mapping of names to indices for a given list.

    Parameters:
        lst (list): The input list of names.

    Returns:
        dict: A dictionary mapping each name to its index in the list.
    """

    return {name: i for i, name in enumerate(lst)}
