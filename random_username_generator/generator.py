import random

def generate_username():
    adjectives = ["happy", "sad", "angry", "brave", "calm", "eager", "fierce", "gentle", "hasty", "jolly"]
    nouns = ["cat", "dog", "bird", "tree", "river", "mountain", "ocean", "city", "forest", "cloud"]
    numbers = [str(i) for i in range(100, 1000)]

    username = f"{random.choice(adjectives)}{random.choice(nouns)}{random.choice(numbers)}"
    return username

if __name__ == "__main__":
    for _ in range(5):
        print(generate_username())
