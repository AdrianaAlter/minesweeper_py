from board import Board

class Game(object):

    lost = False
    revealed_count = 0

    def __init__(self):
        self.board = Board()

    def __repr__(self):
        pass

    def play(self):
        self.setup()
        while self.lost == False and self.revealed_count <= 81:
            self.play_turn()
            self.revealed_count += 1
        if not self.lost:
            self.win()

    def setup(self):
        self.board.place_bombs()
        self.board.assign_values()
        self.display()

    def play_turn(self):
        coordinates = self.get_coordinates()
        choice = self.get_choice()
        self.handle_input(coordinates, choice)
        self.display()

    def get_coordinates(self):
        row = int(raw_input("Choose a row: "))
        column = int(raw_input("Choose a column: "))
        coordinates = [row, column]
        if self.valid_coordinates(coordinates):
            return coordinates
        else:
            self.get_coordinates()

    def get_choice(self):
        choice = raw_input("Flag, reveal, or unflag? Type 'F', 'R', or 'U': ").upper()
        if not self.valid_choice(choice):
            self.get_choice()
        else:
            return choice

    def handle_input(self, coordinates, choice):
        if choice == "R":
            if self.is_bomb(coordinates):
                self.lose()
            else:
                self.reveal(coordinates)
        else:
            self.toggle_flag(coordinates)

    def is_bomb(self, coordinates):
        return self.find(coordinates).bomb

    def display(self):
        print self.board

    def win(self):
        stars = u"\u2728"
        print stars.encode("utf-8") + " Congratulations, you won! " + stars.encode("utf-8")
        self.reveal_all()
        self.display()

    def lose(self):
        fire = u"\u2620"
        print fire.encode("utf-8") + "  Oh no; you made the terminal explode! " + fire.encode("utf-8")
        self.reveal_all()
        self.lost = True

    def reveal_all(self):
        for row in self.board.grid:
            for tile in row:
                tile.flag = False
                tile.revealed = True


    def find(self, coordinates):
        return self.board.grid[coordinates[0]][coordinates[1]]

    def toggle_flag(self, coordinates):
        tile = self.find(coordinates)
        if tile.is_flagged():
            tile.flag = False
        else:
            tile.flag = True

    def reveal(self, coordinates):
        tile = self.find(coordinates)
        tile.revealed = True
        self.revealed_count += 1
        if tile.value == 0:
            [self.handle_input(neighbor, "R") for neighbor in self.board.get_neighbors(coordinates) if self.find(neighbor).revealed == False and self.find(neighbor).bomb == False]

    def valid_coordinates(self, coordinates):
        return len(coordinates) == 2 and coordinates[0] in range(0, 9) and coordinates[1] in range(0, 9)

    def valid_choice(self, choice):
        if choice not in ["F", "R", "U"]:
            return False
        else:
            return True


game = Game()
game.play()
