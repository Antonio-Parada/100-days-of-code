import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Represents the 3x3 board
        self.current_player = 'X'

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_win(self, player):
        # Check rows
        for i in range(3):
            if all(self.board[i*3 + j] == player for j in range(3)):
                return True
        # Check columns
        for i in range(3):
            if all(self.board[i + j*3] == player for j in range(3)):
                return True
        # Check diagonals
        if (self.board[0] == player and self.board[4] == player and self.board[8] == player) or \
           (self.board[2] == player and self.board[4] == player and self.board[6] == player):
            return True
        return False

    def is_board_full(self):
        return ' ' not in self.board

    def play_game(self):
        print("Welcome to Tic Tac Toe!")
        self.print_board()

        while True:
            if self.current_player == 'X':
                try:
                    position = int(input(f"Player {self.current_player}, enter your move (0-8): "))
                    if not (0 <= position <= 8) or not self.make_move(position):
                        print("Invalid move. Try again.")
                        continue
                except ValueError:
                    print("Invalid input. Please enter a number between 0 and 8.")
                    continue
            else:
                # Simple AI for 'O' (random move)
                moves = self.available_moves()
                if moves:
                    position = random.choice(moves)
                    print(f"Player O chooses: {position}")
                    self.make_move(position)
                else:
                    break # No moves left

            self.print_board()

            if self.check_win('X'):
                print("Player X wins!")
                break
            elif self.check_win('O'):
                print("Player O wins!")
                break
            elif self.is_board_full():
                print("It's a tie!")
                break

if __name__ == '__main__':
    game = TicTacToe()
    game.play_game()
