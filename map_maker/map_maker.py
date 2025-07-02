import random
import math
import os
import time

class PerlinNoise:
    def __init__(self, seed=None):
        if seed is not None:
            random.seed(seed)
        self.p = list(range(256))
        random.shuffle(self.p)
        self.p += self.p

    def _fade(self, t):
        return t * t * t * (t * (t * 6 - 15) + 10)

    def _lerp(self, t, a, b):
        return a + t * (b - a)

    def _grad(self, hash, x, y, z):
        h = hash & 15
        u = x if h < 8 else y
        v = y if h < 4 else (x if h == 12 or h == 14 else z)
        return (u if (h & 1) == 0 else -u) + (v if (h & 2) == 0 else -v)

    def noise(self, x, y, z):
        X = math.floor(x) & 255
        Y = math.floor(y) & 255
        Z = math.floor(z) & 255

        x -= math.floor(x)
        y -= math.floor(y)
        z -= math.floor(z)

        u = self._fade(x)
        v = self._fade(y)
        w = self._fade(z)

        A = self.p[X] + Y
        AA = self.p[A] + Z
        AB = self.p[A + 1] + Z
        B = self.p[X + 1] + Y
        BA = self.p[B] + Z
        BB = self.p[B + 1] + Z

        return self._lerp(w, self._lerp(v, self._lerp(u, self._grad(self.p[AA], x, y, z),
                                                    self._grad(self.p[BA], x - 1, y, z)),
                                        self._lerp(u, self._grad(self.p[AB], x, y - 1, z),
                                                    self._grad(self.p[BB], x - 1, y - 1, z))),
                          self._lerp(v, self._lerp(u, self._grad(self.p[AA + 1], x, y, z - 1),
                                                    self._grad(self.p[BA + 1], x - 1, y, z - 1)),
                                        self._lerp(u, self._grad(self.p[AB + 1], x, y - 1, z - 1),
                                                    self._grad(self.p[BB + 1], x - 1, y - 1, z - 1))))

class MapMaker:
    def __init__(self, width=50, height=25, seed=None):
        self.width = width
        self.height = height
        self.noise_generator = PerlinNoise(seed)
        self.map_data = []

    def generate_map(self, scale=10, octaves=1, persistence=0.5, lacunarity=2.0):
        self.map_data = [[0 for _ in range(self.width)] for _ in range(self.height)]

        for y in range(self.height):
            for x in range(self.width):
                amplitude = 1
                frequency = 1
                noise_height = 0

                for _ in range(octaves):
                    noise_height += self.noise_generator.noise(x / scale * frequency, y / scale * frequency, 0) * amplitude
                    amplitude *= persistence
                    frequency *= lacunarity
                
                # Normalize noise to 0-1 range (Perlin noise is typically -1 to 1)
                normalized_noise = (noise_height + 1) / 2
                self.map_data[y][x] = normalized_noise

    def translate_text(self, text):
        words = text.lower().split()
        translated_words = []
        for word in words:
            translated_words.append(self.emoji_map.get(word, word)) # Replace with emoji if found, else keep word
        return " ".join(translated_words)

if __name__ == '__main__':
    translator = EmojiTranslator()

    # Test Case 1: Basic translation
    print("--- Test Case 1: Basic Translation ---")
    text1 = "I am happy and I love pizza"
    translated_text1 = translator.translate_text(text1)
    print(f"Original: {text1}")
    print(f"Translated: {translated_text1}")

    # Test Case 2: Words not in map
    print("
--- Test Case 2: Words Not in Map ---")
    text2 = "This is a test sentence"
    translated_text2 = translator.translate_text(text2)
    print(f"Original: {text2}")
    print(f"Translated: {translated_text2}")

    # Test Case 3: Mixed case and punctuation
    print("
--- Test Case 3: Mixed Case and Punctuation ---")
    text3 = "Hello, I am Sad! Do you like Dogs?"
    translated_text3 = translator.translate_text(text3.replace("!", "").replace("?", "").replace(",", ""))
    print(f"Original: {text3}")
    print(f"Translated: {translated_text3}")
