import random
from tile import Tile

class Board(object):
    bomb_positions = []
    grid = []
    for i in range(9):
        grid.append([])
    for row in grid:
        for i in range(9):
            row.append(Tile())

    def __init__(self):
        pass

    def __repr__(self):
        header = []
        [header.append(self.demarcate(i)) for i in range(9)]
        headerStr = "   " + " ".join(header) + "\n"
        lines = []
        for row in self.grid:
            line = self.demarcate(self.grid.index(row)) + " "
            for tile in row:
                line += str(tile) + " "
            lines.append(line)

        return headerStr +"\n" + "\n\n".join(lines)

    def demarcate(self, num):
        line = u"\u007C"
        return str(num) + line.encode("utf-8")


    def place_bombs(self):
        bomb_count = 0
        while bomb_count < 10:
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            if not [x, y] in self.bomb_positions:
                self.bomb_positions.append([x, y])
                self.grid[x][y].bomb = True
                bomb_count += 1


    def get_neighbors(self, coordinates):
        neighbors = []
        row = coordinates[0]
        column = coordinates[1]
        neighboring_positions = [
            [row - 1, column],
            [row + 1, column],
            [row - 1, column + 1],
            [row, column + 1],
            [row + 1, column + 1],
            [row - 1, column - 1],
            [row, column - 1],
            [row + 1, column - 1]
        ]
        [neighbors.append(pos) for pos in neighboring_positions if self.valid_position(pos)]
        return neighbors

    def valid_position(self, coordinates):
        if coordinates[0] in range(0, 9) and coordinates[1] in range(0, 9):
            return True
        else:
            return False

    def assign_values(self):
        for b_pos in self.bomb_positions:
            for neighbor in self.get_neighbors(b_pos):
                self.grid[neighbor[0]][neighbor[1]].value += 1
