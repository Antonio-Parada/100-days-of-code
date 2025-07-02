import random

class RecipeGenerator:
    def __init__(self):
        self.cuisines = ["Italian", "Mexican", "Indian", "Chinese", "American"]
        self.main_ingredients = ["Chicken", "Beef", "Fish", "Tofu", "Lentils", "Vegetables"]
        self.cooking_methods = ["Grilled", "Baked", "Fried", "Stewed", "Roasted", "Sauteed"]
        self.spices = ["Salt", "Pepper", "Cumin", "Paprika", "Garlic Powder", "Oregano"]
        self.sides = ["Rice", "Noodles", "Potatoes", "Salad", "Bread"]

    def generate_recipe(self):
        cuisine = random.choice(self.cuisines)
        main_ingredient = random.choice(self.main_ingredients)
        cooking_method = random.choice(self.cooking_methods)
        
        num_spices = random.randint(1, 3)
        selected_spices = random.sample(self.spices, num_spices)
        
        num_sides = random.randint(0, 2)
        selected_sides = random.sample(self.sides, num_sides)

        recipe = {
            "Cuisine": cuisine,
            "Main Ingredient": main_ingredient,
            "Cooking Method": cooking_method,
            "Spices": ", ".join(selected_spices) if selected_spices else "None",
            "Sides": ", ".join(selected_sides) if selected_sides else "None"
        }
        return recipe

    def display_recipe(self, recipe):
        print("\n--- Your Generated Recipe ---")
        for key, value in recipe.items():
            print(f"{key}: {value}")
        print("-----------------------------")

if __name__ == '__main__':
    generator = RecipeGenerator()
    print("--- Interactive Recipe Generator ---")
    
    while True:
        recipe = generator.generate_recipe()
        generator.display_recipe(recipe)
        
        user_input = input("Generate another recipe? (y/n): ")
        if user_input.lower() != 'y':
            break

    print("Exiting Recipe Generator.")
