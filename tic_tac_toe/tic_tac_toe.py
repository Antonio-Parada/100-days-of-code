import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, position, player):
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False

    def check_win(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]             # diagonals
        ]
        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return True
        return False

    def is_board_full(self):
        return ' ' not in self.board

    def minimax(self, board, depth, is_maximizing):
        if self.check_win('O'):
            return 1
        elif self.check_win('X'):
            return -1
        elif self.is_board_full():
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for move in self.available_moves():
                self.board[move] = 'O'
                score = self.minimax(self.board, depth + 1, False)
                self.board[move] = ' '
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in self.available_moves():
                self.board[move] = 'X'
                score = self.minimax(self.board, depth + 1, True)
                self.board[move] = ' '
                best_score = min(score, best_score)
            return best_score

    def get_best_move(self):
        best_score = -float('inf')
        best_move = None
        for move in self.available_moves():
            self.board[move] = 'O'
            score = self.minimax(self.board, 0, False)
            self.board[move] = ' '
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def play_game(self, test_moves=None):
        print("Welcome to Tic Tac Toe!")
        self.print_board()
        self.current_player = 'X'

        move_iterator = iter(test_moves) if test_moves else None

        while True:
            if self.current_player == 'X':
                if move_iterator:
                    try:
                        position = next(move_iterator)
                        print(f"Player X chooses: {position}")
                    except StopIteration:
                        print("Test moves exhausted.")
                        break
                else:
                    try:
                        position = int(input(f"Player {self.current_player}, enter your move (0-8): "))
                        if not (0 <= position <= 8):
                            print("Invalid move. Try again.")
                            continue
                    except ValueError:
                        print("Invalid input. Please enter a number between 0 and 8.")
                        continue
                
                if not self.make_move(position, self.current_player):
                    print("Invalid move. Try again.")
                    if not move_iterator:
                        continue
            else:
                position = self.get_best_move()
                print(f"Player O chooses: {position}")
                self.make_move(position, self.current_player)

            self.print_board()

            if self.check_win(self.current_player):
                print(f"Player {self.current_player} wins!")
                break
            elif self.is_board_full():
                print("It's a tie!")
                break

            self.current_player = 'O' if self.current_player == 'X' else 'X'

def run_test():
    game = TicTacToe()
    # A game where X wins
    test_moves = [0, 3, 1, 4, 2]
    game.play_game(test_moves=test_moves)

if __name__ == '__main__':
    import sys
    if '--test' in sys.argv:
        run_test()
    else:
        game = TicTacToe()
        game.play_game()