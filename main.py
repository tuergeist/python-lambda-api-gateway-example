def reverse_it(lines: list) -> list:
    """
    Reverses the line's content. Thus the first char will be the last and the last one the first etc.
    :param lines:
    :return: lines rearanged
    """
    newlines = []
    for line in lines:
        newlines.append(''.join(reversed(line)))
    return newlines
