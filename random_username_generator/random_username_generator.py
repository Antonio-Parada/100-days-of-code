import random

class UsernameGenerator:
    def __init__(self):
        self.adjectives = ["happy", "sad", "brave", "quick", "lazy", "sleepy", "hungry", "clever"]
        self.nouns = ["cat", "dog", "bird", "tree", "river", "mountain", "flower", "star"]

    def generate_username(self, include_numbers=True, num_digits=3):
        adjective = random.choice(self.adjectives)
        noun = random.choice(self.nouns)
        username = f"{adjective.capitalize()}{noun.capitalize()}"

        if include_numbers:
            numbers = ''.join(random.choices("0123456789", k=num_digits))
            username += numbers
        
        return username

if __name__ == '__main__':
    generator = UsernameGenerator()
    print("--- Interactive Random Username Generator ---")
    
    while True:
        include_numbers_input = input("Include numbers? (y/n): ")
        include_numbers = include_numbers_input.lower() == 'y'

        num_digits = 3
        if include_numbers:
            try:
                num_digits_input = input("Number of digits (default 3): ")
                if num_digits_input:
                    num_digits = int(num_digits_input)
            except ValueError:
                print("Invalid input for number of digits. Using default (3).")

        username = generator.generate_username(include_numbers=include_numbers, num_digits=num_digits)
        print(f"Generated Username: {username}")
        
        user_input = input("Generate another username? (y/n): ")
        if user_input.lower() != 'y':
            break

    print("Exiting Username Generator.")
