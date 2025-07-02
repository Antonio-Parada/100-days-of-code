class ChessGame:
    def __init__(self):
        self.board = self.initialize_board()
        self.current_player = 'white'

    def initialize_board(self):
        board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ]
        return board

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def get_piece(self, row, col):
        return self.board[row][col]

    def is_valid_move(self, start_pos, end_pos):
        # Basic validation: check if positions are within board limits
        if not (0 <= start_pos[0] < 8 and 0 <= start_pos[1] < 8 and
                0 <= end_pos[0] < 8 and 0 <= end_pos[1] < 8):
            return False

        piece = self.get_piece(start_pos[0], start_pos[1])
        if piece == ' ':
            return False # No piece at start position

        # Check if it's the current player's piece
        if (self.current_player == 'white' and piece[0] == 'b') or \
           (self.current_player == 'black' and piece[0] == 'w'):
            return False

        # More complex move validation logic for each piece type would go here
        # For now, just allow any move for testing purposes
        return True

    def make_move(self, start_pos, end_pos):
        if self.is_valid_move(start_pos, end_pos):
            piece = self.get_piece(start_pos[0], start_pos[1])
            self.board[end_pos[0]][end_pos[1]] = piece
            self.board[start_pos[0]][start_pos[1]] = ' '
            self.current_player = 'black' if self.current_player == 'white' else 'white'
            return True
        return False

if __name__ == '__main__':
    game = ChessGame()
    game.print_board()
    print(f"Current player: {game.current_player}")

    while True:
        try:
            start_row = int(input("Enter start row: "))
            start_col = int(input("Enter start column: "))
            end_row = int(input("Enter end row: "))
            end_col = int(input("Enter end column: "))

            if game.make_move((start_row, start_col), (end_row, end_col)):
                game.print_board()
                print(f"Current player: {game.current_player}")
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers.")
        except KeyboardInterrupt:
            print("Exiting game.")
            break
