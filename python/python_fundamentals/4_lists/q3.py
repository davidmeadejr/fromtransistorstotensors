def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa

    >>> r = ["Mario", "Browser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Browser", "Mario"]
    """
    racers[0], racers[-1] = racers[-1], racers[0]
    