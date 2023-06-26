def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is
    True if L[i] is greater than thresh, and False otherwise

    >>> Elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    new_list = []

    for l in L:
        if l > thresh
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list