def is_empty_string(string: str) -> bool:
    return string == ''


def is_empty_list(string: str) -> bool:
    return string == []


def is_a_number(string: str) -> bool:
    return string.lstrip('-').replace('.', '', 1).isdigit() and string.count('-') <= 1
