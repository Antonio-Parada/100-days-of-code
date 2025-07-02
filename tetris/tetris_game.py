import random
import time
import os

class TetrisGame:
    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
        self.current_piece = None
        self.piece_x = 0
        self.piece_y = 0
        self.score = 0
        self.game_over = False

        self.shapes = {
            'I': [[(0,0), (0,1), (0,2), (0,3)], [(0,0), (1,0), (2,0), (3,0)]], # I-shape
            'J': [[(0,1), (1,1), (2,1), (2,0)], [(0,0), (0,1), (1,0), (2,0)], [(0,0), (0,1), (1,1), (2,1)], [(0,1), (1,1), (2,1), (0,0)]], # J-shape
            'L': [[(0,0), (1,0), (2,0), (2,1)], [(0,0), (0,1), (1,1), (2,1)], [(0,1), (1,1), (2,1), (0,0)], [(0,0), (1,0), (2,0), (0,1)]], # L-shape
            'O': [[(0,0), (0,1), (1,0), (1,1)]], # O-shape
            'S': [[(0,1), (1,0), (1,1), (2,0)], [(0,0), (1,0), (1,1), (2,1)]], # S-shape
            'T': [[(0,0), (1,0), (1,1), (2,0)], [(0,0), (0,1), (1,0), (2,0)], [(0,1), (1,0), (1,1), (2,1)], [(0,1), (1,1), (2,0), (2,1)]], # T-shape
            'Z': [[(0,0), (1,0), (1,1), (2,1)], [(0,1), (1,0), (1,1), (2,0)]]  # Z-shape
        }
        self.colors = {
            'I': 'C', 'J': 'B', 'L': 'O', 'O': 'Y', 'S': 'G', 'T': 'P', 'Z': 'R'
        }
        self.current_rotation = 0
        self._new_piece()

    def _new_piece(self):
        shape_name = random.choice(list(self.shapes.keys()))
        self.current_piece = self.shapes[shape_name][0] # Start with first rotation
        self.piece_x = self.width // 2 - 2
        self.piece_y = 0
        self.current_rotation = 0
        self.current_piece_name = shape_name

        if not self._is_valid_position(self.current_piece, self.piece_x, self.piece_y):
            self.game_over = True

    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _draw_board(self):
        self._clear_screen()
        display_board = [row[:] for row in self.board] # Create a copy

        # Draw current piece
        for dx, dy in self.current_piece:
            x, y = self.piece_x + dx, self.piece_y + dy
            if 0 <= x < self.width and 0 <= y < self.height:
                display_board[y][x] = self.colors[self.current_piece_name]

        print("Score: ", self.score)
        for row in display_board:
            print('|' + ''.join(row) + '|')
        print('+' + '-' * self.width + '+')

    def _is_valid_position(self, piece, x, y):
        for dx, dy in piece:
            board_x, board_y = x + dx, y + dy
            if not (0 <= board_x < self.width and 0 <= board_y < self.height and self.board[board_y][board_x] == ' '):
                return False
        return True

    def _rotate_piece(self):
        next_rotation = (self.current_rotation + 1) % len(self.shapes[self.current_piece_name])
        new_piece = self.shapes[self.current_piece_name][next_rotation]
        if self._is_valid_position(new_piece, self.piece_x, self.piece_y):
            self.current_piece = new_piece
            self.current_rotation = next_rotation

    def _move_piece(self, dx, dy):
        if self._is_valid_position(self.current_piece, self.piece_x + dx, self.piece_y + dy):
            self.piece_x += dx
            self.piece_y += dy
            return True
        return False

    def _lock_piece(self):
        for dx, dy in self.current_piece:
            x, y = self.piece_x + dx, self.piece_y + dy
            self.board[y][x] = self.colors[self.current_piece_name]

    def _clear_lines(self):
        lines_cleared = 0
        new_board = []
        for y in range(self.height):
            if ' ' not in self.board[y]: # Line is full
                lines_cleared += 1
                new_board.insert(0, [' ' for _ in range(self.width)]) # Add empty line at top
            else:
                new_board.append(self.board[y])
        
        # Pad with empty lines at the top if lines were cleared
        while len(new_board) < self.height:
            new_board.insert(0, [' ' for _ in range(self.width)])

        self.board = new_board
        self.score += lines_cleared * 100 # Simple scoring

    def play_game(self):
        print("Welcome to Tetris!")
        print("Controls: A/D for left/right, S for down, W for rotate. Q to quit.")
        time.sleep(2)

        while not self.game_over:
            self._draw_board()
            time.sleep(0.5) # Piece fall speed

            if not self._move_piece(0, 1): # Try to move down
                self._lock_piece()
                self._clear_lines()
                self._new_piece()

            # In a real game, you'd handle user input here
            # For now, it just falls automatically

        print("Game Over! Final Score: ", self.score)

if __name__ == '__main__':
    game = TetrisGame()
    game.play_game()
