GEAR: str = "*"

class Gear:
    """
    Represents a gear in the grid
    Really just used to save the number of neighbors and its value in memory
    """
    def __init__(self) -> None:
        self.val = 1
        self.neighbors = 0

class EngineNumber:
    """
    Represents an EngineNumber
    The coords are the (row, col) of all its string values, left to right
    The val is the int parsed value of that string from the grid
    """
    def __init__(self, val: int, coords: list[tuple]) -> None:
        self.val = val
        self.coords = coords

    def update_gears(self, grid: list[str], gears: dict[tuple, Gear]) -> None:
        """
        Gets the neighbors for the engine number
        If any of the neighbors is a GEAR, update that related Gear object
        """
        neighbors: set[tuple] = set()   # Made a set because we only want uniques
        for coord in self.coords:
            for neighbor in get_neighbors(*coord, grid):
                neighbors.add(neighbor)
        
        for neighbor in neighbors:
            nrow, ncol = neighbor
            if grid[nrow][ncol] == "*":
                gears[(nrow, ncol)].neighbors += 1
                gears[(nrow, ncol)].val *= self.val


def get_neighbors(row: int, col: int, grid: list[str]) -> list[tuple]:
    """
    Gets all valid neighbors of the given coordinates
    Max possible is 8: E, NE, N, NW, W, SW, S, SE
    """
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
    #       With this loop also keep track of all Gears found and put it in a map
    #       Then loop through the EngineNumbers, get their neighbors, and if any are a gear
    #       update that related Gear object with the information about the EngineNumber
    #       At the end, only add up Gear object values that have 2 neighbors


    file = open("./input.txt", encoding="utf-8")
    lines: list[str] = file.read().splitlines()
    file.close()


    # keep track of the engine numbers found
    engine_numbers: list[EngineNumber] = []

    # gears is important because it maps the (row, col) to a gear object
    # makes it easy to look up stored information about a gear
    gears: dict[tuple, Gear] = {}

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

            if curr == GEAR:
                gears[(row, col)] = Gear()

            col += 1

        # Don't miss end number
        if (number and coords):
            engine_numbers.append(EngineNumber(int(number), coords))

        row += 1

    # Now with all engine coords and gears, determine if the engine coord is valid and add to total
    total: int = 0

    # This will update the values of all gears
    for engine_number in engine_numbers:
        engine_number.update_gears(lines, gears)

    # Only sum up gears that have only 2 neighbors
    for coord, gear in gears.items():
        if gear.neighbors == 2:
            total += gear.val

    print(total)
