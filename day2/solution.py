# # P1
# if __name__ == "__main__":
#     file = open("./input.txt", encoding="utf-8")
#     lines: list[str] = file.read().splitlines()
#     file.close()

#     # Track max amount of cubes
#     colors: dict[str, int] = {
#         "red": 12,
#         "green": 13,
#         "blue": 14 
#     }

#     total: int = 0

#     for line in lines:
#         # Need to parse
#         game_id: int = int(line.split(':')[0].split(' ')[1])

#         subsets: list[str] = line.split(':')[1].strip().split(';')

#         is_valid_game: bool = True

#         for subset in subsets:
#             cubes: list[str] = subset.strip().split(',')

#             for cube in cubes:
#                 amount: int = int(cube.strip().split(' ')[0])
#                 color: str = cube.strip().split(' ')[1]

#                 if amount > colors[color]:
#                     is_valid_game = False
#                     break

#             if not is_valid_game:
#                 break

#         if is_valid_game:
#             total += game_id

#     print(total)


# P2
if __name__ == "__main__":
    file = open("./input.txt", encoding="utf-8")
    lines: list[str] = file.read().splitlines()
    file.close()

    total: int = 0

    for line in lines:
        # Keep track of the min amount needed per game
        colors: dict[str, int] = {
            "red": -1,
            "green": -1,
            "blue": -1
        }

        # Need to parse each line
        game_id: int = int(line.split(':')[0].split(' ')[1])

        subsets: list[str] = line.split(':')[1].strip().split(';')

        for subset in subsets:
            cubes: list[str] = subset.strip().split(',')

            for cube in cubes:
                amount: int = int(cube.strip().split(' ')[0])
                color: str = cube.strip().split(' ')[1]

                colors[color] = max(colors[color], amount)
            
        total += (colors["red"] * colors["green"] * colors["blue"])

    print(total)