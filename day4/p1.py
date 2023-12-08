
if __name__ == "__main__":
    # Idea: Parse the input, get the two lists for each card
    #       Find the intersection between the two
    #       2^(len(intersection) - 1) is the answer for that card
    #       Sum them all up

    file = open("./input.txt", encoding="utf-8")
    lines: list[str] = file.read().splitlines()
    file.close()

    total: int = 0

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

        if len(intersection) != 0:
            total += 2**(len(intersection) - 1)

    print(total)
