
if __name__ == "__main__":
    # Idea: Parse the input, get the two lists for each card
    #       Find the intersection between the two
    #       2^(len(intersection) - 1) is the answer for that card
    #       Sum them all up

    #       Essentially same idea, but do a bit of dp
    #

    file = open("./input.txt", encoding="utf-8")
    lines: list[str] = file.read().splitlines()
    file.close()

    total: int = 0

    round_values: list[int] = [0] * len(lines)
    num_cards: list[int] = [1] * len(lines)

    # Get the winner values
    idx: int = 0
    for line in lines:
        # This is so annoying
        line = line.replace("  ", " ")
        line = line.replace("   ", " ")
        line = line.replace("    ", " ")

        groups: list[str] = line.split(":")[1].strip().split("|")
        group1: list[int] = [int(val) for val in groups[0].strip().split(" ")]
        group2: list[int] = [int(val) for val in groups[1].strip().split(" ")]

        winners: set = set(group1)
        numbers: set = set(group2)

        intersection: set = winners.intersection(numbers)

        round_values[idx] = len(intersection)

        idx += 1

    
    # Count up how many cards of each there will be
    for idx, val in enumerate(round_values):
        for card_idx in range(idx + 1, idx + 1 + val):
            if card_idx >= len(round_values):
                break

            num_cards[card_idx] += num_cards[idx]

    print(sum(num_cards))
