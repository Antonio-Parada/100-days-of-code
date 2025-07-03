import random
import time

class MemoryPuzzleGame:
    def __init__(self, rows=4, cols=4):
        self.rows = rows
        self.cols = cols
        self.board = self._generate_board()
        self.revealed = [[False for _ in range(cols)] for _ in range(rows)]
        self.selected_cards = []
        self.matches_found = 0
        self.attempts = 0

    def _generate_board(self):
        # Create pairs of cards
        num_pairs = (self.rows * self.cols) // 2
        card_values = [chr(ord('A') + i) for i in range(num_pairs)] * 2
        random.shuffle(card_values)

        board = []
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                row.append(card_values.pop())
            board.append(row)
        return board

    def display_board(self):
        print("  " + " ".join(str(i) for i in range(self.cols)))
        for r_idx, row in enumerate(self.board):
            display_row = []
            for c_idx, card in enumerate(row):
                if self.revealed[r_idx][c_idx]:
                    display_row.append(card)
                else:
                    display_row.append('#')
            print(f"{r_idx} {' '.join(display_row)}")

    def select_card(self, row, col):
        if not (0 <= row < self.rows and 0 <= col < self.cols) or self.revealed[row][col]:
            print("Invalid selection. Try again.")
            return False

        self.revealed[row][col] = True
        self.selected_cards.append((row, col))

        if len(self.selected_cards) == 2:
            self.attempts += 1
            self.display_board()
            time.sleep(1) # Briefly show the second card

            card1_pos = self.selected_cards[0]
            card2_pos = self.selected_cards[1]

            if self.board[card1_pos[0]][card1_pos[1]] == self.board[card2_pos[0]][card2_pos[1]]:
                print("Match found!")
                self.matches_found += 1
            else:
                print("No match. Cards will be flipped back.")
                self.revealed[card1_pos[0]][card1_pos[1]] = False
                self.revealed[card2_pos[0]][card2_pos[1]] = False
            self.selected_cards = []
            return True
        return True

    def check_win(self):
        return self.matches_found == (self.rows * self.cols) // 2

    def play_game(self):
        print("Memory Puzzle Game Started!")
        while not self.check_win():
            self.display_board()
            print(f"Attempts: {self.attempts}")
            try:
                row1 = int(input("Enter row for first card: "))
                col1 = int(input("Enter column for first card: "))
                if not self.select_card(row1, col1):
                    continue

                self.display_board()
                row2 = int(input("Enter row for second card: "))
                col2 = int(input("Enter column for second card: "))
                if not self.select_card(row2, col2):
                    # If second selection is invalid, revert first card
                    self.revealed[row1][col1] = False
                    self.selected_cards = []
                    continue

            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

        self.display_board()
        print(f"Congratulations! You won in {self.attempts} attempts!")

if __name__ == "__main__":
    game = MemoryPuzzleGame()
    game.play_game()
