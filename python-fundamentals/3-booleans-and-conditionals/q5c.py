def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    """

    return (ketchup and not mustard) or (mustard and not ketchup)