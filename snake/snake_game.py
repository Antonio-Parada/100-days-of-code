import random
import time
import os

class SnakeGame:
    def __init__(self, width=20, height=10):
        self.width = width
        self.height = height
        self.snake = [(width // 2, height // 2)]
        self.food = self._generate_food()
        self.direction = 'RIGHT'
        self.score = 0
        self.game_over = False

    def _generate_food(self):
        while True:
            food_pos = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if food_pos not in self.snake:
                return food_pos

    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _draw_board(self):
        self._clear_screen()
        print("Score: ", self.score)
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) == self.food:
                    print('F', end=' ')
                elif (x, y) in self.snake:
                    print('S', end=' ')
                else:
                    print('.', end=' ')
            print()

    def _move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == 'UP':
            new_head = (head_x, head_y - 1)
        elif self.direction == 'DOWN':
            new_head = (head_x, head_y + 1)
        elif self.direction == 'LEFT':
            new_head = (head_x - 1, head_y)
        elif self.direction == 'RIGHT':
            new_head = (head_x + 1, head_y)

        self.snake.insert(0, new_head)

        # Check for collisions
        if (new_head[0] < 0 or new_head[0] >= self.width or
            new_head[1] < 0 or new_head[1] >= self.height or
            new_head in self.snake[1:]):
            self.game_over = True
            return

        # Check for food
        if new_head == self.food:
            self.score += 1
            self.food = self._generate_food()
        else:
            self.snake.pop()

    def play_interactive(self):
        print("Welcome to Snake Game!")
        print("Use W, A, S, D to move. Press Q to quit.")
        time.sleep(2)

        while not self.game_over:
            self._draw_board()
            self._move_snake()
            time.sleep(0.2) # Adjust speed

            # In a real interactive game, you'd get input here
            # For this CLI version, we'll just keep moving in the current direction
            # until a collision or food is found.

        print("Game Over! Your score: ", self.score)

if __name__ == '__main__':
    game = SnakeGame()
    game.play_interactive()