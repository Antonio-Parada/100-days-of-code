class ChessBoard:
    def __init__(self):
        self.board = self._initialize_board()

    def _initialize_board(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        # Place pawns
        for i in range(8):
            board[1][i] = Pawn("black", (1, i))
            board[6][i] = Pawn("white", (6, i))
        # Place rooks
        board[0][0] = Rook("black", (0, 0))
        board[0][7] = Rook("black", (0, 7))
        board[7][0] = Rook("white", (7, 0))
        board[7][7] = Rook("white", (7, 7))
        # Place knights
        board[0][1] = Knight("black", (0, 1))
        board[0][6] = Knight("black", (0, 6))
        board[7][1] = Knight("white", (7, 1))
        board[7][6] = Knight("white", (7, 6))
        # Place bishops
        board[0][2] = Bishop("black", (0, 2))
        board[0][5] = Bishop("black", (0, 5))
        board[7][2] = Bishop("white", (7, 2))
        board[7][5] = Bishop("white", (7, 5))
        # Place queens
        board[0][3] = Queen("black", (0, 3))
        board[7][3] = Queen("white", (7, 3))
        # Place kings
        board[0][4] = King("black", (0, 4))
        board[7][4] = King("white", (7, 4))
        return board

    def display_board(self):
        for row in self.board:
            row_str = ""
            for piece in row:
                if piece:
                    row_str += piece.symbol + " "
                else:
                    row_str += ". "
            print(row_str)

class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.symbol = ""

    def is_valid_move(self, board, new_position):
        raise NotImplementedError

class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = "bP" if color == "black" else "wP"

    def is_valid_move(self, board, new_position):
        current_row, current_col = self.position
        new_row, new_col = new_position

        # Determine direction based on color
        direction = 1 if self.color == "black" else -1

        # Single square move forward
        if new_col == current_col and new_row == current_row + direction:
            return board[new_row][new_col] is None

        # Two square initial move forward
        if (self.color == "black" and current_row == 1 and new_row == current_row + 2 * direction) or \
           (self.color == "white" and current_row == 6 and new_row == current_row + 2 * direction):
            if new_col == current_col and board[new_row][new_col] is None and board[current_row + direction][current_col] is None:
                return True

        # Diagonal capture
        if abs(new_col - current_col) == 1 and new_row == current_row + direction:
            target_piece = board[new_row][new_col]
            return target_piece is not None and target_piece.color != self.color

        return False

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = "bR" if color == "black" else "wR"

    def is_valid_move(self, new_position):
        return True

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = "bN" if color == "black" else "wN"

    def is_valid_move(self, new_position):
        return True

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = "bB" if color == "black" else "wB"

    def is_valid_move(self, new_position):
        return True

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = "bQ" if color == "black" else "wQ"

    def is_valid_move(self, new_position):
        return True

class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = "bK" if color == "black" else "wK"

    def is_valid_move(self, new_position):
        return True

class ChessGame:
    def __init__(self):
        self.board = ChessBoard()
        self.current_player = "white"

    def make_move(self, start_pos, end_pos):
        # Simplified move logic for now
        piece = self.board.board[start_pos[0]][start_pos[1]]
        if piece and piece.color == self.current_player and piece.is_valid_move(self.board.board, end_pos):
            self.board.board[end_pos[0]][end_pos[1]] = piece
            self.board.board[start_pos[0]][start_pos[1]] = None
            piece.position = end_pos
            self.switch_player()
            return True
        return False

    def switch_player(self):
        self.current_player = "black" if self.current_player == "white" else "white"

    def play_game(self):
        print("Chess Game Started!")
        while True:
            self.board.display_board()
            print(f"\n{self.current_player}'s turn.")
            # Placeholder for player input and move validation
            # For now, just break after a few turns for demonstration
            break

if __name__ == "__main__":
    game = ChessGame()
    game.play_game()