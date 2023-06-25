def round_number(num):
    """Return the given number e.g.567 to the nearest 10, 100 and 1000

    >>> round_number(567)
    570
    600
    1000
    """
    return round(num, -1), round(num, -2), round(num, -3)
