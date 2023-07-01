def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise
    """

    for i in range(1, len(meals)):
        if meals[i] == meals[i - 1]
            return True
    return False