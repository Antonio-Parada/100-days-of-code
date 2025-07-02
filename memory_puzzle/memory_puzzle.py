import random
import time
import os

class MemoryPuzzle:
    def __init__(self, rows=4, cols=4):
        self.rows = rows
        self.cols = cols
        self.board = []
        self.revealed = [[False for _ in range(cols)] for _ in range(rows)]
        self.generate_board()
        self.matched_pairs = 0
        self.attempts = 0

    def generate_board(self):
        # Create pairs of characters
        num_pairs = (self.rows * self.cols) // 2
        characters = [chr(ord('A') + i) for i in range(num_pairs)]
        cards = characters * 2
        random.shuffle(cards)

        # Populate the board
        self.board = []
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                row.append(cards.pop())
            self.board.append(row)

    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_board(self):
        self._clear_screen()
        print("Memory Puzzle")
        print("Attempts: ", self.attempts)
        print("  " + " ".join([str(i) for i in range(self.cols)]))
        print(" --" + "--" * self.cols)
        for r in range(self.rows):
            print(f"{r}| ", end="")
            for c in range(self.cols):
                if self.revealed[r][c]:
                    print(self.board[r][c], end=" ")
                else:
                    print('#', end=" ")
            print()

    def get_move(self):
        while True:
            try:
                row1 = int(input("Enter row for first card: "))
                col1 = int(input("Enter column for first card: "))
                row2 = int(input("Enter row for second card: "))
                col2 = int(input("Enter column for second card: "))

                if not (0 <= row1 < self.rows and 0 <= col1 < self.cols and
                        0 <= row2 < self.rows and 0 <= col2 < self.cols):
                    print("Invalid coordinates. Try again.")
                    continue
                if (row1, col1) == (row2, col2):
                    print("Cannot select the same card twice. Try again.")
                    continue
                if self.revealed[row1][col1] or self.revealed[row2][col2]:
                    print("One or both cards are already revealed. Try again.")
                    continue
                return (row1, col1), (row2, col2)
            except ValueError:
                print("Invalid input. Please enter numbers.")

    def play_game(self, simulated_moves=None):
        print("Welcome to Memory Puzzle!")
        time.sleep(1)

        move_idx = 0
        while self.matched_pairs < (self.rows * self.cols) // 2:
            self.display_board()
            
            if simulated_moves and move_idx < len(simulated_moves):
                (r1, c1), (r2, c2) = simulated_moves[move_idx]
                print(f"Simulating move: ({r1},{c1}) and ({r2},{c2})")
                move_idx += 1
            else:
                print("No more simulated moves. Exiting test.")
                break

            self.attempts += 1

            # Check if selected cards are valid for revealing
            if not (0 <= r1 < self.rows and 0 <= c1 < self.cols and
                    0 <= r2 < self.rows and 0 <= c2 < self.cols and
                    (r1, c1) != (r2, c2) and
                    not self.revealed[r1][c1] and not self.revealed[r2][c2]):
                print("Invalid simulated move. Skipping.")
                time.sleep(1)
                continue

            self.revealed[r1][c1] = True
            self.revealed[r2][c2] = True
            self.display_board()
            time.sleep(0.5) # Show cards for a moment

            if self.board[r1][c1] == self.board[r2][c2]:
                print("Match!")
                self.matched_pairs += 1
            else:
                print("No match.")
                self.revealed[r1][c1] = False
                self.revealed[r2][c2] = False
            time.sleep(0.5)

        self.display_board()
        print(f"Congratulations! You matched all pairs in {self.attempts} attempts.")

if __name__ == '__main__':
    # Test Case 1: Perfect game (assuming a 2x2 board for simplicity)
    print("\n--- Test Case 1: Perfect Game (2x2) ---")
    game1 = MemoryPuzzle(rows=2, cols=2)
    # Manually set a predictable board for testing
    game1.board = [['A', 'B'], ['A', 'B']]
    game1.play_game(simulated_moves=[
        ((0,0), (1,0)), # Match A
        ((0,1), (1,1))  # Match B
    ])

    # Test Case 2: Some mismatches
    print("\n--- Test Case 2: With Mismatches (2x2) ---")
    game2 = MemoryPuzzle(rows=2, cols=2)
    game2.board = [['A', 'B'], ['C', 'A']]
    game2.play_game(simulated_moves=[
        ((0,0), (0,1)), # A vs B (Mismatch)
        ((0,0), (1,1)), # A vs A (Match)
        ((0,1), (1,0))  # B vs C (Mismatch)
    ])
