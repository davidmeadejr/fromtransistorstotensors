def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword.
    Returns list of the index values into the original list for all documents
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, "casino")
    >>> [0]
    """

    # list to hold the indices of matching documents
    indices = []
    # Iterate through the indices (i) and elements (doc) of documents
    for i, doc in enumerate(doc_list):
        # Split the string doc into a list of words (according to whitespace)
        tokens = doc.split()
        # Make a transformed list where we "normalise" each word to facilitate matching.
        # Periods and commas are removed from the end of each word to facilitate matching.
        normalised = [token.strip(".,").lower() for token in tokens]
        # Is there a match? If so, update the list of matching indices
        if keyword.lower() in normalised:
            indices.append(i)
    return indices