import random

class Snake:
    def __init__(self):
        self.body = [(10, 10), (10, 9), (10, 8)]  # Initial snake body
        self.direction = "RIGHT"  # Initial direction

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == "UP":
            new_head = (head_x - 1, head_y)
        elif self.direction == "DOWN":
            new_head = (head_x + 1, head_y)
        elif self.direction == "LEFT":
            new_head = (head_x, head_y - 1)
        elif self.direction == "RIGHT":
            new_head = (head_x, head_y + 1)
        self.body.insert(0, new_head)
        self.body.pop()  # Remove tail

    def change_direction(self, new_direction):
        if new_direction == "UP" and self.direction != "DOWN":
            self.direction = new_direction
        elif new_direction == "DOWN" and self.direction != "UP":
            self.direction = new_direction
        elif new_direction == "LEFT" and self.direction != "RIGHT":
            self.direction = new_direction
        elif new_direction == "RIGHT" and self.direction != "LEFT":
            self.direction = new_direction

class Food:
    def __init__(self, game_width, game_height):
        self.position = self._generate_position(game_width, game_height)

    def _generate_position(self, game_width, game_height):
        return (random.randint(0, game_width - 1), random.randint(0, game_height - 1))

class Game:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.snake = Snake()
        self.food = Food(self.width, self.height)
        self.score = 0
        self.game_over = False

    def update(self):
        if self.game_over:
            return

        self.snake.move()

        # Check for collision with food
        if self.snake.body[0] == self.food.position:
            self.score += 1
            self.snake.body.append(self.snake.body[-1])  # Grow snake
            self.food.position = self.food._generate_position(self.width, self.height)

        # Check for collision with walls
        head_x, head_y = self.snake.body[0]
        if not (0 <= head_x < self.width and 0 <= head_y < self.height):
            self.game_over = True

        # Check for collision with self
        if self.snake.body[0] in self.snake.body[1:]:
            self.game_over = True

    def display(self):
        # Create an empty grid
        grid = [['.' for _ in range(self.width)] for _ in range(self.height)]

        # Place snake on grid
        for segment_x, segment_y in self.snake.body:
            grid[segment_x][segment_y] = 'S'

        # Place food on grid
        food_x, food_y = self.food.position
        grid[food_x][food_y] = 'F'

        # Print the grid
        for row in grid:
            print(' '.join(row))
        print(f"Score: {self.score}")
        if self.game_over:
            print("GAME OVER!")

    def run(self):
        while not self.game_over:
            self.display()
            self.update()
            # In a real game, you'd have a delay here and handle user input
            # For now, it will run very fast.
            # input("Press Enter to continue...") # Uncomment for step-by-step

from snake_ai.snake_ai import SnakeAI

if __name__ == "__main__":
    game = Game()
    ai = SnakeAI(game)
    while not game.game_over:
        game.display()
        next_move = ai.get_next_move()
        if next_move:
            game.snake.change_direction(next_move)
            game.update()
        else:
            print("AI has no valid moves. Game Over.")
            break
    game.display() # Display final state
