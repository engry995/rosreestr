import re
from typing import Optional
from .models import BaseObject

def get_numbers_from_file(file) -> list:

    numbers = []
    for line in file:
        line = line.decode('utf-8')
        line = line.strip()
        if re.fullmatch(r"\d{1,8}:\d{1,8}:\d{1,8}:\d{1,8}", line):
            numbers.append(line)
    return numbers


def add_numbers_to_base(numbers: list, type_of_object: str,
                        parent: Optional[BaseObject] = None) -> None:
    """
    Parameters
    ----------
    numbers
    type_of_object
    parent
    Returns (всего номеров, успешно загружено, количество повторных номеров)
    -------

    """

    new_entry = [BaseObject(number=num, type_object=type_of_object) for num in numbers]
    BaseObject.objects.bulk_create(new_entry, ignore_conflicts=True)
    return
