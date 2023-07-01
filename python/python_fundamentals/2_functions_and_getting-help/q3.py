def to_smash(total_candies, number_of_friends=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between a given number of friends. If the
    the number of friends has not been given, assume the number of friends is 3.

    >>> to_smash(91)
    1
    """
    return total_candies % number_of_friends