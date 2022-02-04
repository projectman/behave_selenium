from typing import List

import yaml


def read_yaml(file_name: str) -> dict:
    """
    :param file_name: str, relative path to file
    :return: string data?
    """
    with open(file_name, 'r') as yf:
        data_out = yaml.safe_load(yf)
    return data_out


def lists_have_equal_elements(list_1: List, list_2: List) -> bool:
    """
    It compares 2 lists of string, numbers, or mixture. Length must be equal and
    every element must be equal, for string lowercase
    @param: list_1, List of number, strings or mixture
    @param: list_2, List of number, strings or mixture

    @returns: bool, True if the list are equal and False if not equal
    """
    if len(list_1) != len(list_2):
        return False

    sorted_1 = sorted(list_1)
    sorted_2 = sorted(list_2)

    res = [el_1 == el_2 for el_1, el_2 in zip(sorted_1, sorted_2)]

    return all(res)


if __name__ == '__main__':
    lists_have_equal_elements([3, 4, 1], [1, 4, 4])