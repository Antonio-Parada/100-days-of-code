import random
import os

class BattleshipGame:
    def __init__(self, size=10):
        self.size = size
        self.player1_board = self._create_empty_board()
        self.player2_board = self._create_empty_board()
        self.player1_ships = self._place_ships(self.player1_board)
        self.player2_ships = self._place_ships(self.player2_board)
        self.current_player = 1
        self.game_over = False

    def _create_empty_board(self):
        return [['~' for _ in range(self.size)] for _ in range(self.size)]

    def _place_ships(self, board):
        ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
        placed_ships = {}

        for ship_name, ship_length in ships.items():
            while True:
                orientation = random.choice(['H', 'V']) # H for horizontal, V for vertical
                
                if orientation == 'H':
                    if ship_length > self.size: # Ship too long for board
                        continue
                    row = random.randint(0, self.size - 1)
                    col = random.randint(0, self.size - ship_length)
                else:
                    if ship_length > self.size: # Ship too long for board
                        continue
                    row = random.randint(0, self.size - ship_length)
                    col = random.randint(0, self.size - 1)

                # Check if placement is valid
                valid_placement = True
                temp_coords = []
                for i in range(ship_length):
                    if orientation == 'H':
                        if board[row][col + i] != '~':
                            valid_placement = False
                            break
                        temp_coords.append((row, col + i))
                    else:
                        if board[row + i][col] != '~':
                            valid_placement = False
                            break
                        temp_coords.append((row + i, col))
                
                if valid_placement:
                    # Place the ship
                    for r, c in temp_coords:
                        board[r][c] = 'S'
                    placed_ships[ship_name] = temp_coords
                    break
        return placed_ships

    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _display_board(self, board, hide_ships=True):
        print("  " + " ".join([str(i) for i in range(self.size)]))
        for r_idx, row in enumerate(board):
            display_row = []
            for cell in row:
                if hide_ships and cell == 'S':
                    display_row.append('~')
                else:
                    display_row.append(cell)
            print(f"{r_idx} {' '.join(display_row)}")

    def take_shot(self, target_player_board, target_player_ships, row, col):
        if not (0 <= row < self.size and 0 <= col < self.size):
            return "Invalid coordinates."

        if target_player_board[row][col] in ['X', 'O']:
            return "Already shot there."

        if target_player_board[row][col] == 'S':
            target_player_board[row][col] = 'X' # Hit
            # Check if ship is sunk
            sunk_ship = None
            for ship_name, coords in target_player_ships.items():
                if (row, col) in coords:
                    all_hit = True
                    for r, c in coords:
                        if target_player_board[r][c] != 'X':
                            all_hit = False
                            break
                    if all_hit:
                        sunk_ship = ship_name
                        break
            if sunk_ship:
                return f"Hit and sunk {sunk_ship}!"
            else:
                return "Hit!"
        else:
            target_player_board[row][col] = 'O' # Miss
            return "Miss."

    def check_game_over(self, player_board, player_ships):
        for ship_name, coords in player_ships.items():
            for r, c in coords:
                if player_board[r][c] == 'S': # Check if any part of the ship is still 'S' (not hit)
                    return False # Game is not over
        return True # All ships sunk

    def play_game_non_interactive(self, player1_shots, player2_shots):
        print("--- Non-Interactive Battleship Test ---")
        print("Player 1's Board (Hidden Ships):")
        self._display_board(self.player1_board)
        print("\nPlayer 2's Board (Hidden Ships):")
        self._display_board(self.player2_board)

        shot_idx1 = 0
        shot_idx2 = 0

        while True:
            # Player 1's turn
            if shot_idx1 < len(player1_shots):
                row, col = player1_shots[shot_idx1]
                print(f"\nPlayer 1 shoots at ({row},{col})")
                result = self.take_shot(self.player2_board, self.player2_ships, row, col)
                print(f"Result: {result}")
                self._display_board(self.player2_board, hide_ships=False) # Show hits/misses
                shot_idx1 += 1
                if self.check_game_over(self.player2_board, self.player2_ships):
                    print("Player 1 wins!")
                    break
            else:
                print("Player 1 has no more shots.")
                break

            # Player 2's turn
            if shot_idx2 < len(player2_shots):
                row, col = player2_shots[shot_idx2]
                print(f"\nPlayer 2 shoots at ({row},{col})")
                result = self.take_shot(self.player1_board, self.player1_ships, row, col)
                print(f"Result: {result}")
                self._display_board(self.player1_board, hide_ships=False)
                shot_idx2 += 1
                if self.check_game_over(self.player1_board, self.player1_ships):
                    print("Player 2 wins!")
                    break
            else:
                print("Player 2 has no more shots.")
                break

        if self.check_game_over(self.player1_board, self.player1_ships) and self.check_game_over(self.player2_board, self.player2_ships):
            print("It's a draw!")

if __name__ == '__main__':
    # Test Case 1: Player 1 sinks all of Player 2's ships
    print("\n--- Test Case 1: Player 1 Wins ---")
    game1 = BattleshipGame(size=5) # Smaller board for easier testing
    player1_shots = []
    player2_shots = []

    # Find all coordinates of Player 2's ships and add them to player1_shots
    for ship_name, coords in game1.player2_ships.items():
        for r, c in coords:
            player1_shots.append((r, c))
    
    game1.play_game_non_interactive(player1_shots, player2_shots)

    # Test Case 2: Game ends in a draw (no more ships, no winner)
    print("\n--- Test Case 2: Draw Game ---")
    game2 = BattleshipGame(size=3)
    player1_shots_draw = []
    player2_shots_draw = []

    # Hit one part of each ship for a draw scenario
    for ship_name, coords in game2.player1_ships.items():
        player2_shots_draw.append(coords[0])
    for ship_name, coords in game2.player2_ships.items():
        player1_shots_draw.append(coords[0])

    game2.play_game_non_interactive(player1_shots_draw, player2_shots_draw)
