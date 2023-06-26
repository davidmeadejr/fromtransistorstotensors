def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    # Access the element which is at the point of half of the list
    # If the name is found in the list after the middle_index and is not the last element return "fashionable late"
    # else return not fashionable late

    order = arrivals.index(name)
    return order >=len(arrivals) / 2 and order != len(arrivals) - 1 