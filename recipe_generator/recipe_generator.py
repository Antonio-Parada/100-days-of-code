import random

class RecipeGenerator:
    def __init__(self):
        self.recipes = {
            "italian": [
                {"name": "Pasta Carbonara", "ingredients": ["pasta", "eggs", "bacon", "parmesan"]},
                {"name": "Margherita Pizza", "ingredients": ["pizza dough", "tomato sauce", "mozzarella", "basil"]},
            ],
            "mexican": [
                {"name": "Tacos", "ingredients": ["tortillas", "ground beef", "lettuce", "cheese", "salsa"]},
                {"name": "Guacamole", "ingredients": ["avocado", "onion", "cilantro", "lime", "jalapeno"]},
            ],
            "indian": [
                {"name": "Chicken Tikka Masala", "ingredients": ["chicken", "yogurt", "tomatoes", "spices"]},
                {"name": "Lentil Dal", "ingredients": ["lentils", "onions", "tomatoes", "spices"]},
            ],
        }

    def generate_recipe_by_cuisine(self, cuisine):
        cuisine = cuisine.lower()
        if cuisine in self.recipes:
            return random.choice(self.recipes[cuisine])
        return None

    def generate_random_recipe(self):
        cuisine = random.choice(list(self.recipes.keys()))
        return self.generate_recipe_by_cuisine(cuisine)

if __name__ == "__main__":
    generator = RecipeGenerator()

    print("Random Recipe:")
    recipe = generator.generate_random_recipe()
    if recipe:
        print(f"Name: {recipe['name']}")
        print(f"Ingredients: {', '.join(recipe['ingredients'])}")
    else:
        print("Could not generate a recipe.")

    print("\nItalian Recipe:")
    italian_recipe = generator.generate_recipe_by_cuisine("italian")
    if italian_recipe:
        print(f"Name: {italian_recipe['name']}")
        print(f"Ingredients: {', '.join(italian_recipe['ingredients'])}")
    else:
        print("Could not generate an Italian recipe.")