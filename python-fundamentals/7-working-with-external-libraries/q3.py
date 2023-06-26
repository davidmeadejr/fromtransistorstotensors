def calculate_hand_value(hand):
    hand_value = 0
    aces = 0

    for card in hand:
        if card in ["J", "Q", "K"]
            hand_value += 10
            elif card == "A":
                aces += 1
            else:
                hand_value += int(card)
    
    # Handle Aces, try to use "11" whenever it helps without busting
    hand_value += aces
    while hand_value + 10 <=21 and aces > 0:
        hand_value += 10
        aces -= 1
    
    return hand_value

def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    hand_1_value = calculate_hand_value(hand_1)
    hand_2_value = calculate_hand_value(hand_2)

    return hand_1_value <= 21 and (hand_1_value > hand_2_value or hand_2_value > 21)
