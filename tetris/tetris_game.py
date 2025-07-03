import random

class Tetromino:
    SHAPES = {
        "I": [['C', 'C', 'C', 'C']],
        "J": [['C', '.', '.'], ['C', 'C', 'C']],
        "L": [['.', '.', 'C'], ['C', 'C', 'C']],
        "O": [['C', 'C'], ['C', 'C']],
        "S": [['.', 'C', 'C'], ['C', 'C', '.']],
        "T": [['.', 'C', '.'], ['C', 'C', 'C']],
        "Z": [['C', 'C', '.'], ['.', 'C', 'C']],
    }

    def __init__(self, shape_type):
        self.shape_type = shape_type
        self.shape = self.SHAPES[shape_type]
        self.color = 'C' # Placeholder for color
        self.row = 0
        self.col = 3 # Initial column for new pieces

    def rotate(self):
        # Simple rotation (90 degrees clockwise)
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

class TetrisGame:
    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.grid = self._create_empty_grid()
        self.current_piece = self._new_piece()
        self.game_over = False
        self.score = 0

    def _create_empty_grid(self):
        return [['.' for _ in range(self.width)] for _ in range(self.height)]

    def _new_piece(self):
        shape_type = random.choice(list(Tetromino.SHAPES.keys()))
        return Tetromino(shape_type)

    def _check_collision(self, piece, row_offset=0, col_offset=0):
        for r_idx, row in enumerate(piece.shape):
            for c_idx, cell in enumerate(row):
                if cell != '.':
                    grid_row = piece.row + r_idx + row_offset
                    grid_col = piece.col + c_idx + col_offset
                    if not (0 <= grid_row < self.height and 0 <= grid_col < self.width) or \
                       self.grid[grid_row][grid_col] != '.':
                        return True
        return False

    def _merge_piece(self, piece):
        for r_idx, row in enumerate(piece.shape):
            for c_idx, cell in enumerate(row):
                if cell != '.':
                    self.grid[piece.row + r_idx][piece.col + c_idx] = piece.color

    def _clear_lines(self):
        lines_cleared = 0
        new_grid = [['.' for _ in range(self.width)] for _ in range(self.height)]
        current_row = self.height - 1
        for r in range(self.height - 1, -1, -1):
            if '.' not in self.grid[r]:
                lines_cleared += 1
            else:
                new_grid[current_row] = self.grid[r]
                current_row -= 1
        self.grid = new_grid
        self.score += lines_cleared ** 2 # Simple scoring

    def move_piece(self, direction):
        if self.game_over:
            return

        if direction == "left":
            if not self._check_collision(self.current_piece, col_offset=-1):
                self.current_piece.col -= 1
        elif direction == "right":
            if not self._check_collision(self.current_piece, col_offset=1):
                self.current_piece.col += 1
        elif direction == "down":
            if not self._check_collision(self.current_piece, row_offset=1):
                self.current_piece.row += 1
            else:
                self._merge_piece(self.current_piece)
                self._clear_lines()
                self.current_piece = self._new_piece()
                if self._check_collision(self.current_piece):
                    self.game_over = True

    def rotate_piece(self):
        if self.game_over:
            return
        original_shape = self.current_piece.shape
        self.current_piece.rotate()
        if self._check_collision(self.current_piece):
            self.current_piece.shape = original_shape # Revert if collision

    def display_grid(self):
        for r_idx, row in enumerate(self.grid):
            display_row = []
            for c_idx, cell in enumerate(row):
                if self.current_piece and r_idx >= self.current_piece.row and r_idx < self.current_piece.row + len(self.current_piece.shape) and \
                   c_idx >= self.current_piece.col and c_idx < self.current_piece.col + len(self.current_piece.shape[0]):
                    
                    piece_cell = self.current_piece.shape[r_idx - self.current_piece.row][c_idx - self.current_piece.col]
                    if piece_cell != '.':
                        display_row.append(piece_cell)
                    else:
                        display_row.append(cell)
                else:
                    display_row.append(cell)
            print(' '.join(display_row))
        print(f"Score: {self.score}")
        if self.game_over:
            print("GAME OVER!")

    def run(self):
        print("Tetris Game Started!")
        while not self.game_over:
            self.display_grid()
            self.move_piece("down") # Auto move down for now
            # In a real game, you'd handle user input and a game tick delay
            # For now, it will run very fast.
            # import time
            # time.sleep(0.5)

if __name__ == "__main__":
    game = TetrisGame()
    game.run()