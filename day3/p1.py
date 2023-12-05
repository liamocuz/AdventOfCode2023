# P1

class EngineNumber:
    def __init__(self, val: int, coords: list[tuple]) -> None:
        self.val = val
        self.coords = coords

    def is_valid(self, grid: list[str]) -> bool:
        for coord in self.coords:
            row, col = coord
            neighbors: list[tuple] = self.get_neighbors(row, col, grid)
            for neighbor in neighbors:
                nrow, ncol = neighbor
                ncurr = grid[nrow][ncol]
                if not ncurr.isdigit() and ncurr != '.':
                    return True

        return False


    def get_neighbors(self, row: int, col: int, grid: list[str]) -> list[tuple]:
        ROW_MAX: int = len(grid)
        COL_MAX: int = len(grid[0])

        def valid_neighbor(coord) -> bool:
            row, col = coord
            return (row >= 0 and row < ROW_MAX and col >= 0 and col < COL_MAX)

        neighbors: list[tuple] = [
            (row + 1, col),
            (row - 1, col),
            (row, col + 1),
            (row, col - 1),
            (row + 1, col + 1),
            (row + 1, col - 1),
            (row - 1, col + 1),
            (row - 1, col - 1),
        ]

        return list(filter(valid_neighbor, neighbors))



if __name__ == "__main__":
    # Idea: Loop through each line looking for a number
    #       Find all coordinates of that number, and parse it into an int
    #       Search at each coordinate and check all surrounding spots looking for a part symbol
    #       If at least one of the coordinates has a part symbol neighbor, add the number


    file = open("./input.txt", encoding="utf-8")
    lines: list[str] = file.read().splitlines()
    file.close()


    engine_numbers: list[EngineNumber] = []

    # Use row and col ints
    row: int = 0
    col: int = 0

    # Get all engine numbers and their coordinates
    while row < len(lines):
        col = 0

        number: str = ""
        coords: list[tuple] = []

        while col < len(lines[0]):
            curr: str = lines[row][col]

            if curr.isdigit():
                number += curr
                coords.append((row, col))
            elif (number and coords):
                engine_numbers.append(EngineNumber(int(number), coords))
                number = ""
                coords = []

            col += 1

        # Don't miss end number
        if (number and coords):
            engine_numbers.append(EngineNumber(int(number), coords))

        row += 1

    # Now with all engine coords, determine if the engine coord is valid and add to total
    total: int = 0

    for engine_number in engine_numbers:
        if engine_number.is_valid(lines):
            total += engine_number.val

    print(total)
