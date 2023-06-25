def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.

    >>> to_smash(91)
    >>> to_smash(1)
    Splitting 91 candies
    Splitting 1 candy
    """
    if total_candies == 1:
        print("Splitting", total_candies, "candy")
    else: 
        print("Splitting", total_candies, "candies")