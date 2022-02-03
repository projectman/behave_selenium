import yaml


def read_yaml(file_name: str) -> dict:
    """
    :param file_name: str, relative path to file
    :return: string data?
    """
    with open(file_name, 'r') as yf:
        data_out = yaml.safe_load(yf)
    return data_out
