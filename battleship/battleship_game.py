class Board:
    def __init__(self, size=10):
        self.size = size
        self.grid = [['.' for _ in range(size)] for _ in range(size)]
        self.ships = []

    def display(self, reveal_ships=False):
        print("  " + " ".join(str(i) for i in range(self.size)))
        for r_idx, row in enumerate(self.grid):
            display_row = []
            for c_idx, cell in enumerate(row):
                if not reveal_ships and cell in ['S']:
                    display_row.append('.')
                else:
                    display_row.append(cell)
            print(f"{r_idx} {' '.join(display_row)}")

    def place_ship(self, ship, start_row, start_col, orientation):
        # Simplified placement for now, no collision detection
        if orientation == "horizontal":
            for i in range(ship.length):
                self.grid[start_row][start_col + i] = 'S'
        else: # vertical
            for i in range(ship.length):
                self.grid[start_row + i][start_col] = 'S'
        self.ships.append(ship)

    def receive_shot(self, row, col):
        if self.grid[row][col] == 'S':
            self.grid[row][col] = 'X' # Hit
            return True
        else:
            self.grid[row][col] = 'O' # Miss
            return False

class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.hits = 0

    def is_sunk(self):
        return self.hits == self.length

class BattleshipGame:
    def __init__(self):
        self.player_board = Board()
        self.computer_board = Board()
        self.player_ships = self._create_ships()
        self.computer_ships = self._create_ships()

    def _create_ships(self):
        return [
            Ship("Carrier", 5),
            Ship("Battleship", 4),
            Ship("Cruiser", 3),
            Ship("Submarine", 3),
            Ship("Destroyer", 2),
        ]

    def setup_game(self):
        # Place player ships (manual for now)
        print("Place your ships:")
        for ship in self.player_ships:
            while True:
                try:
                    print(f"Placing {ship.name} (Length: {ship.length})")
                    start_row = int(input("Enter start row: "))
                    start_col = int(input("Enter start column: "))
                    orientation = input("Enter orientation (horizontal/vertical): ")
                    self.player_board.place_ship(ship, start_row, start_col, orientation)
                    self.player_board.display(reveal_ships=True)
                    break
                except (ValueError, IndexError):
                    print("Invalid input. Try again.")

        # Place computer ships (random for now)
        import random
        for ship in self.computer_ships:
            while True:
                try:
                    start_row = random.randint(0, self.computer_board.size - 1)
                    start_col = random.randint(0, self.computer_board.size - 1)
                    orientation = random.choice(["horizontal", "vertical"])
                    # Simplified placement, no collision detection for computer
                    self.computer_board.place_ship(ship, start_row, start_col, orientation)
                    break
                except (ValueError, IndexError):
                    continue

    def play_game(self):
        print("Battleship Game Started!")
        self.setup_game()

        while True:
            print("\n--- Your Board ---")
            self.player_board.display(reveal_ships=True)
            print("\n--- Computer's Board (Hidden) ---")
            self.computer_board.display()

            # Player's turn
            while True:
                try:
                    shot_row = int(input("Enter row to shoot: "))
                    shot_col = int(input("Enter column to shoot: "))
                    if 0 <= shot_row < self.player_board.size and 0 <= shot_col < self.player_board.size:
                        if self.computer_board.receive_shot(shot_row, shot_col):
                            print("Hit!")
                        else:
                            print("Miss!")
                        break
                    else:
                        print("Invalid coordinates. Try again.")
                except ValueError:
                    print("Invalid input. Enter numbers for row and column.")

            # Check if all computer ships are sunk
            if all(ship.is_sunk() for ship in self.computer_ships):
                print("You sunk all computer ships! You win!")
                break

            # Computer's turn (random shot for now)
            while True:
                shot_row = random.randint(0, self.player_board.size - 1)
                shot_col = random.randint(0, self.player_board.size - 1)
                if self.player_board.receive_shot(shot_row, shot_col):
                    print(f"Computer hit your ship at ({shot_row}, {shot_col})!")
                    break
                else:
                    print(f"Computer missed at ({shot_row}, {shot_col}).")
                    break

            # Check if all player ships are sunk
            if all(ship.is_sunk() for ship in self.player_ships):
                print("All your ships are sunk! Computer wins!")
                break

if __name__ == "__main__":
    game = BattleshipGame()
    game.play_game()