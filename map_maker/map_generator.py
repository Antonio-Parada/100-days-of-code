import random
import noise

class MapGenerator:
    def __init__(self, width, height, scale=10.0, octaves=6, persistence=0.5, lacunarity=2.0, seed=None):
        self.width = width
        self.height = height
        self.scale = scale
        self.octaves = octaves
        self.persistence = persistence
        self.lacunarity = lacunarity
        self.seed = seed if seed is not None else random.randint(0, 100000)
        random.seed(self.seed)

    def generate_map(self):
        game_map = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for r in range(self.height):
            for c in range(self.width):
                # Generate Perlin noise value
                value = noise.pnoise2(r / self.scale, c / self.scale,
                                      octaves=self.octaves,
                                      persistence=self.persistence,
                                      lacunarity=self.lacunarity,
                                      repeatx=1024,
                                      repeaty=1024,
                                      base=self.seed)
                
                # Normalize to 0-1 and then threshold for land/water
                # You might need to adjust the threshold based on desired land/water ratio
                if value > 0:
                    game_map[r][c] = 1 # Land
                else:
                    game_map[r][c] = 0 # Water
        return game_map

    def display_map(self, game_map):
        for row in game_map:
            print(' '.join(['~' if cell == 0 else '#' for cell in row]))

if __name__ == "__main__":
    map_gen = MapGenerator(width=50, height=20, scale=50.0, octaves=4, persistence=0.5, lacunarity=2.0)
    new_map = map_gen.generate_map()
    map_gen.display_map(new_map)