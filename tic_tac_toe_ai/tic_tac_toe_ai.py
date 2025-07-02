import math

class TicTacToeAI:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.ai_player = 'O'
        self.human_player = 'X'

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self, board):
        return [i for i, spot in enumerate(board) if spot == ' ']

    def make_move(self, board, position, player):
        if board[position] == ' ':
            board[position] = player
            return True
        return False

    def check_win(self, board, player):
        # Check rows
        for i in range(3):
            if all(board[i*3 + j] == player for j in range(3)):
                return True
        # Check columns
        for i in range(3):
            if all(board[i + j*3] == player for j in range(3)):
                return True
        # Check diagonals
        if (board[0] == player and board[4] == player and board[8] == player) or \
           (board[2] == player and board[4] == player and board[6] == player):
            return True
        return False

    def is_board_full(self, board):
        return ' ' not in board

    def minimax(self, board, player):
        max_player = self.ai_player  # 'O'
        other_player = self.human_player  # 'X'

        if self.check_win(board, max_player):
            return {'score': 1}
        if self.check_win(board, other_player):
            return {'score': -1}
        if self.is_board_full(board):
            return {'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in self.available_moves(board):
            # Step 1: make a move, try that spot
            self.make_move(board, possible_move, player)

            # Step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(board, other_player)  # now we alternate players

            # Step 3: undo the move
            board[possible_move] = ' '

            # Step 4: update the best
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best

    def play_game(self):
        print("Welcome to Tic Tac Toe AI!")
        self.print_board()

        while not self.is_board_full(self.board):
            if self.current_player == self.human_player:
                # Human player chooses a random valid move for testing
                moves = self.available_moves(self.board)
                if moves:
                    position = random.choice(moves)
                    print(f"Player {self.human_player} chooses: {position}")
                    self.make_move(self.board, position, self.human_player)
                else:
                    break
            else:
                print(f"Player {self.ai_player} is thinking...")
                # AI makes move
                move = self.minimax(self.board[:], self.ai_player)['position'] # Pass a copy of the board
                self.make_move(self.board, move, self.ai_player)
                print(f"Player {self.ai_player} chooses: {move}")

            self.print_board()

            if self.check_win(self.board, self.human_player):
                print("You win!")
                break
            elif self.check_win(self.board, self.ai_player):
                print("AI wins!")
                break

            self.current_player = self.ai_player if self.current_player == self.human_player else self.human_player

        if self.is_board_full(self.board) and not self.check_win(self.board, self.human_player) and not self.check_win(self.board, self.ai_player):
            print("It's a tie!")

if __name__ == '__main__':
    game = TicTacToeAI()
    game.play_game()
