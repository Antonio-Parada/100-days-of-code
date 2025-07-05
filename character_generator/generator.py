import random

class Character:
    def __init__(self, name, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Strength: {self.strength}\n" \
               f"Dexterity: {self.dexterity}\n" \
               f"Constitution: {self.constitution}\n" \
               f"Intelligence: {self.intelligence}\n" \
               f"Wisdom: {self.wisdom}\n" \
               f"Charisma: {self.charisma}"

def generate_random_name():
    first_names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
    last_names = ["Smith", "Jones", "Williams", "Brown", "Davis", "Miller"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_attribute_score():
    return random.randint(8, 18)

def generate_character():
    name = generate_random_name()
    strength = generate_attribute_score()
    dexterity = generate_attribute_score()
    constitution = generate_attribute_score()
    intelligence = generate_attribute_score()
    wisdom = generate_attribute_score()
    charisma = generate_attribute_score()
    return Character(name, strength, dexterity, constitution, intelligence, wisdom, charisma)

if __name__ == "__main__":
    for _ in range(3):
        character = generate_character()
        print(character)
        print("\n" + "-"*20 + "\n")
