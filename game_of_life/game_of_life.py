import time
import os
import random

class GameOfLife:
    def __init__(self, width=40, height=20, wrap_around=True):
        self.width = width
        self.height = height
        self.grid = self._create_empty_grid()
        self.wrap_around = wrap_around

    def _create_empty_grid(self):
        return [[0 for _ in range(self.width)] for _ in range(self.height)]

    def seed_grid_randomly(self, density=0.2):
        for y in range(self.height):
            for x in range(self.width):
                if random.random() < density:
                    self.grid[y][x] = 1

    def seed_grid_pattern(self, pattern, start_x, start_y):
        for dy, row in enumerate(pattern):
            for dx, cell in enumerate(row):
                x, y = start_x + dx, start_y + dy
                if 0 <= x < self.width and 0 <= y < self.height:
                    self.grid[y][x] = cell

    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_grid(self):
        self._clear_screen()
        for y in range(self.height):
            print(''.join(['#' if cell == 1 else ' ' for cell in self.grid[y]]))

    def _get_live_neighbors(self, x, y):
        live_neighbors = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue

                nx, ny = x + dx, y + dy

                if self.wrap_around:
                    nx = (nx + self.width) % self.width
                    ny = (ny + self.height) % self.height

                if 0 <= nx < self.width and 0 <= ny < self.height:
                    live_neighbors += self.grid[ny][nx]
        return live_neighbors

    def update_generation(self):
        new_grid = self._create_empty_grid()
        for y in range(self.height):
            for x in range(self.width):
                live_neighbors = self._get_live_neighbors(x, y)
                current_cell = self.grid[y][x]

                if current_cell == 1: # Live cell
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[y][x] = 0 # Dies
                    else:
                        new_grid[y][x] = 1 # Lives
                else: # Dead cell
                    if live_neighbors == 3:
                        new_grid[y][x] = 1 # Becomes alive
        self.grid = new_grid

    def run_simulation(self, generations=50):
        print("--- Conway's Game of Life ---")
        print("Randomly seeded grid. Press Ctrl+C to stop.")
        self.seed_grid_randomly()

        for gen in range(generations):
            self.display_grid()
            self.update_generation()
            time.sleep(0.1)

        print("Simulation finished.")

if __name__ == '__main__':
    game = GameOfLife()
    game.run_simulation()
