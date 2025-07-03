import random

class ChessAI:
    def __init__(self, game):
        self.game = game

    def get_random_move(self):
        valid_moves = []
        for r in range(8):
            for c in range(8):
                piece = self.game.board.board[r][c]
                if piece and piece.color == self.game.current_player:
                    for new_r in range(8):
                        for new_c in range(8):
                            if piece.is_valid_move(self.game.board.board, (new_r, new_c)):
                                valid_moves.append(((r, c), (new_r, new_c)))
        if valid_moves:
            return random.choice(valid_moves)
        return None

if __name__ == "__main__":
    # This part is for testing the AI independently
    # In a real scenario, the ChessGame would use this AI
    pass
