def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    total_payout = 0

    for i in range(n_runs):
        payout = play_slot_machine() - 1
        total_payout += payout

    avg_payout = total_payout / n_runs
    return avg_payout

### List Comprehension Alternative
def estimate_average_slot_payout(n_runs):
    # Play slot machine n_runs times, calculate payout of each 
    payouts = [play_slot_machine() - 1 for i in range(n_runs)]
    # Calculate the average value
    avg_payout = sum(payouts) / n_runs
    return avg_payout