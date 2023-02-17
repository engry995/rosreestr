import re

def get_numbers_from_file(file) -> list:

    numbers = []
    for line in file:
        line = line.decode('utf-8')
        line = line.strip()
        if re.fullmatch(r"\d{1,8}:\d{1,8}:\d{1,8}:\d{1,8}", line):
            numbers.append(line)
    return numbers


def add_numbers_to_base(numbers: list, type_of_object: str) -> tuple[int, int, int]:
    """
    Parameters
    ----------
    numbers
    type_of_object

    Returns (всего номеров, успешно загружено, количество повторных номеров)
    -------

    """

    return 25, 5, 10

    