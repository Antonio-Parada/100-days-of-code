class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-----')

    def is_valid_move(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' '

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def check_win(self, player):
        # Check rows
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        # Check columns
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        # Check diagonals
        if (self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player) or \
           (self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player):
            return True
        return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

class TicTacToeGame:
    def __init__(self):
        self.board = Board()
        self.current_player = 'X'
        self.game_over = False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_game(self):
        print("Tic Tac Toe Game Started!")
        while not self.game_over:
            self.board.display()
            print(f"Player {self.current_player}'s turn.")
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if self.board.is_valid_move(row, col):
                self.board.make_move(row, col, self.current_player)
                if self.board.check_win(self.current_player):
                    self.board.display()
                    print(f"Player {self.current_player} wins!")
                    self.game_over = True
                elif self.board.check_draw():
                    self.board.display()
                    print("It's a draw!")
                    self.game_over = True
                else:
                    self.switch_player()
            else:
                print("Invalid move. Try again.")

if __name__ == "__main__":
    game = TicTacToeGame()
    game.play_game()
