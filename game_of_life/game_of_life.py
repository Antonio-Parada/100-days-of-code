import random
import time
import os

class GameOfLife:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = self._create_random_grid()

    def _create_random_grid(self):
        return [[random.choice([0, 1]) for _ in range(self.width)] for _ in range(self.height)]

    def _get_neighbors(self, x, y):
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                nx, ny = x + i, y + j
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    neighbors.append(self.grid[ny][nx])
        return neighbors

    def update_grid(self):
        new_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                live_neighbors = sum(self._get_neighbors(x, y))
                if self.grid[y][x] == 1:  # Live cell
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[y][x] = 0  # Dies
                    else:
                        new_grid[y][x] = 1  # Lives
                else:  # Dead cell
                    if live_neighbors == 3:
                        new_grid[y][x] = 1  # Becomes alive
        self.grid = new_grid

    def display_grid(self):
        os.system('cls' if os.name == 'nt' else 'clear') # Clear console
        for row in self.grid:
            print(''.join(['#' if cell == 1 else ' ' for cell in row]))

    def run_simulation(self, generations=100):
        for i in range(generations):
            print(f"Generation: {i+1}")
            self.display_grid()
            self.update_grid()
            time.sleep(0.1)

if __name__ == "__main__":
    game = GameOfLife(width=40, height=20)
    game.run_simulation()