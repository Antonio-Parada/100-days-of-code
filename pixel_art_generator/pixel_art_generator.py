import random
import os
import time

class PixelArtGenerator:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.grid = self._create_empty_grid()

    def _create_empty_grid(self):
        return [[0 for _ in range(self.width)] for _ in range(self.height)]

    def generate_random_art(self, density=0.5):
        for y in range(self.height):
            for x in range(self.width):
                if random.random() < density:
                    self.grid[y][x] = 1 # Represent a colored pixel
                else:
                    self.grid[y][x] = 0 # Represent an empty pixel

    def display_art(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(self.height):
            row_chars = []
            for x in range(self.width):
                if self.grid[y][x] == 1:
                    row_chars.append('██') # Filled block
                else:
                    row_chars.append('  ') # Empty block
            print(''.join(row_chars))

if __name__ == '__main__':
    generator = PixelArtGenerator(width=30, height=15)
    print("--- Interactive Pixel Art Generator ---")
    
    while True:
        generator.generate_random_art(density=random.uniform(0.1, 0.9))
        generator.display_art()
        
        user_input = input("Generate another random art? (y/n): ")
        if user_input.lower() != 'y':
            break

    print("Exiting Pixel Art Generator.")
