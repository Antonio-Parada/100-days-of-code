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

    def is_valid_move(self, board, new_position):
        current_row, current_col = self.position
        new_row, new_col = new_position

        # Rook moves horizontally or vertically
        if current_row == new_row:  # Horizontal move
            step = 1 if new_col > current_col else -1
            for col in range(current_col + step, new_col, step):
                if board[current_row][col] is not None:
                    return False  # Path is blocked
        elif current_col == new_col:  # Vertical move
            step = 1 if new_row > current_row else -1
            for row in range(current_row + step, new_row, step):
                if board[row][current_col] is not None:
                    return False  # Path is blocked
        else:
            return False  # Invalid move for Rook

        target_piece = board[new_row][new_col]
        return target_piece is None or target_piece.color != self.color

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = "bN" if color == "black" else "wN"

    def is_valid_move(self, board, new_position):
        current_row, current_col = self.position
        new_row, new_col = new_position

        row_diff = abs(new_row - current_row)
        col_diff = abs(new_col - current_col)

        # Knight moves in an L-shape: 2 squares in one direction (horizontal or vertical)
        # and 1 square in the perpendicular direction.
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            target_piece = board[new_row][new_col]
            return target_piece is None or target_piece.color != self.color
        return False

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = "bB" if color == "black" else "wB"

    def is_valid_move(self, board, new_position):
        current_row, current_col = self.position
        new_row, new_col = new_position

        row_diff = new_row - current_row
        col_diff = new_col - current_col

        if abs(row_diff) != abs(col_diff):
            return False  # Not a diagonal move

        row_step = 1 if row_diff > 0 else -1
        col_step = 1 if col_diff > 0 else -1

        # Check if path is clear
        r, c = current_row + row_step, current_col + col_step
        while r != new_row and c != new_col:
            if board[r][c] is not None:
                return False  # Path is blocked
            r += row_step
            c += col_step

        target_piece = board[new_row][new_col]
        return target_piece is None or target_piece.color != self.color

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = "bQ" if color == "black" else "wQ"

    def is_valid_move(self, board, new_position):
        current_row, current_col = self.position
        new_row, new_col = new_position

        row_diff = new_row - current_row
        col_diff = new_col - current_col

        # Check for Rook-like moves (horizontal or vertical)
        if current_row == new_row:  # Horizontal move
            step = 1 if new_col > current_col else -1
            for col in range(current_col + step, new_col, step):
                if board[current_row][col] is not None:
                    return False  # Path is blocked
            target_piece = board[new_row][new_col]
            return target_piece is None or target_piece.color != self.color
        elif current_col == new_col:  # Vertical move
            step = 1 if new_row > current_row else -1
            for row in range(current_row + step, new_row, step):
                if board[row][current_col] is not None:
                    return False  # Path is blocked
            target_piece = board[new_row][new_col]
            return target_piece is None or target_piece.color != self.color

        # Check for Bishop-like moves (diagonal)
        elif abs(row_diff) == abs(col_diff):
            row_step = 1 if row_diff > 0 else -1
            col_step = 1 if col_diff > 0 else -1

            r, c = current_row + row_step, current_col + col_step
            while r != new_row and c != new_col:
                if board[r][c] is not None:
                    return False  # Path is blocked
                r += row_step
                c += col_step

            target_piece = board[new_row][new_col]
            return target_piece is None or target_piece.color != self.color

        return False

class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = "bK" if color == "black" else "wK"

    def is_valid_move(self, board, new_position):
        current_row, current_col = self.position
        new_row, new_col = new_position

        row_diff = abs(new_row - current_row)
        col_diff = abs(new_col - current_col)

        # King can move one square in any direction
        if row_diff <= 1 and col_diff <= 1:
            target_piece = board[new_row][new_col]
            return target_piece is None or target_piece.color != self.color
        return False

from chess_ai.chess_ai import ChessAI

class ChessGame:
    def __init__(self):
        self.board = ChessBoard()
        self.current_player = "white"
        self.ai = ChessAI(self)

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
            if self.current_player == "white":
                # Placeholder for human player input
                print("Enter your move (e.g., 'e2 e4'):")
                move_str = input()
                try:
                    start_col = ord(move_str[0]) - ord('a')
                    start_row = 8 - int(move_str[1])
                    end_col = ord(move_str[3]) - ord('a')
                    end_row = 8 - int(move_str[4])
                    start_pos = (start_row, start_col)
                    end_pos = (end_row, end_col)
                    if not self.make_move(start_pos, end_pos):
                        print("Invalid move. Try again.")
                except (ValueError, IndexError):
                    print("Invalid input format. Please use 'e.g., e2 e4'.")
            else:
                print("AI is thinking...")
                ai_move = self.ai.get_random_move()
                if ai_move:
                    start_pos, end_pos = ai_move
                    self.make_move(start_pos, end_pos)
                    print(f"AI moves from {chr(ord('a') + start_pos[1])}{8 - start_pos[0]} to {chr(ord('a') + end_pos[1])}{8 - end_pos[0]}")
                else:
                    print("AI has no valid moves. Game over.")
                    self.game_over = True
            
            if self.game_over:
                break

if __name__ == "__main__":
    game = ChessGame()
    game.play_game()