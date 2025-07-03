import random
import sys
sys.path.append('../snake') # Add parent directory to path to import snake_game
from snake_game import Game, Snake

class SnakeAI:
    def __init__(self, game):
        self.game = game

    def get_next_move(self):
        # For now, a simple random valid move
        possible_moves = ["UP", "DOWN", "LEFT", "RIGHT"]
        random.shuffle(possible_moves)

        for move in possible_moves:
            original_direction = self.game.snake.direction
            original_head = self.game.snake.body[0]
            original_body = list(self.game.snake.body) # Create a copy

            self.game.snake.change_direction(move)
            self.game.snake.move() # Simulate move

            head_x, head_y = self.game.snake.body[0]

            # Check for collisions in simulated move
            collision_with_wall = not (0 <= head_x < self.game.width and 0 <= head_y < self.game.height)
            collision_with_self = self.game.snake.body[0] in self.game.snake.body[1:]

            # Revert snake state
            self.game.snake.direction = original_direction
            self.game.snake.body = original_body

            if not collision_with_wall and not collision_with_self:
                return move
        return None # No valid moves found

if __name__ == "__main__":
    # Example Usage (requires a Game instance)
    game = Game()
    ai = SnakeAI(game)
    
    # Simulate a few moves
    for _ in range(10):
        game.display()
        next_move = ai.get_next_move()
        if next_move:
            game.snake.change_direction(next_move)
            game.update()
        else:
            print("AI has no valid moves. Game Over.")
            break
