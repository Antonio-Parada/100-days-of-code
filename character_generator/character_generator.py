import random

class CharacterGenerator:
    def __init__(self):
        self.first_names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Heidi"]
        self.last_names = ["Smith", "Jones", "Williams", "Brown", "Davis", "Miller", "Wilson", "Moore"]
        self.classes = ["Warrior", "Mage", "Rogue", "Cleric"]
        self.races = ["Human", "Elf", "Dwarf", "Orc"]

    def generate_name(self):
        first = random.choice(self.first_names)
        last = random.choice(self.last_names)
        return f"{first} {last}"

    def generate_stats(self):
        stats = {
            "Strength": random.randint(8, 18),
            "Dexterity": random.randint(8, 18),
            "Constitution": random.randint(8, 18),
            "Intelligence": random.randint(8, 18),
            "Wisdom": random.randint(8, 18),
            "Charisma": random.randint(8, 18),
        }
        return stats

    def generate_character(self):
        name = self.generate_name()
        char_class = random.choice(self.classes)
        race = random.choice(self.races)
        stats = self.generate_stats()

        character = {
            "Name": name,
            "Race": race,
            "Class": char_class,
            "Stats": stats
        }
        return character

    def display_character(self, character):
        print("\n--- Character Sheet ---")
        for key, value in character.items():
            if isinstance(value, dict):
                print(f"{key}:")
                for stat, val in value.items():
                    print(f"  {stat}: {val}")
            else:
                print(f"{key}: {value}")
        print("-----------------------")

if __name__ == '__main__':
    generator = CharacterGenerator()
    print("--- Interactive Character Generator ---")
    
    while True:
        character = generator.generate_character()
        generator.display_character(character)
        
        user_input = input("Generate another character? (y/n): ")
        if user_input.lower() != 'y':
            break

    print("Exiting Character Generator.")
