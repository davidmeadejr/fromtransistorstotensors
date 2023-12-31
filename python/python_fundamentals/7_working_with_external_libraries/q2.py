# Import luigi's full dataset of race data
from learntools.python.luigi_analysis import full_dataset

def best_items(racers):
    winner_item_counts = {}
    for i in range(len(racers)):
        # The i'th racer dictionary
        racer = racers[i]
        # We're only interested in racers who finished in first
        if racer['finish'] == 1:
            for item in racer["items"]:
                # Add one to the count for this item (adding it to the dict if necessary)
                if i not in winner_item_counts:
                    winner_item_counts[i] = 0
                winner_item_counts[i] += 1
        # Data quality issue :/ Print a warning about racers with no name set. We'll take care of it later.
        if racer["name"] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                i+1, len(racers), racer["name"])
                )
    return winner_item_counts