class CalorieCounter:
    def __init__(self):
        self.food_database = {
            "apple": {"calories": 95, "protein": 0.5, "carbs": 25, "fat": 0.3},
            "banana": {"calories": 105, "protein": 1.3, "carbs": 27, "fat": 0.3},
            "chicken breast": {"calories": 165, "protein": 31, "carbs": 0, "fat": 3.6},
            "rice": {"calories": 130, "protein": 2.7, "carbs": 28, "fat": 0.3},
            "egg": {"calories": 78, "protein": 6, "carbs": 0.6, "fat": 5.3}
        }
        self.daily_log = []

    def add_food(self, food_name, quantity=1):
        food_name_lower = food_name.lower()
        if food_name_lower in self.food_database:
            food_info = self.food_database[food_name_lower]
            self.daily_log.append({
                'name': food_name_lower,
                'quantity': quantity,
                'calories': food_info['calories'] * quantity,
                'protein': food_info['protein'] * quantity,
                'carbs': food_info['carbs'] * quantity,
                'fat': food_info['fat'] * quantity
            })
            print(f"Added {quantity} {food_name} to your log.")
        else:
            print(f"Food '{food_name}' not found in database.")

    def get_daily_summary(self):
        total_calories = 0
        total_protein = 0
        total_carbs = 0
        total_fat = 0

        for item in self.daily_log:
            total_calories += item['calories']
            total_protein += item['protein']
            total_carbs += item['carbs']
            total_fat += item['fat']

        print("\n--- Daily Summary ---")
        if not self.daily_log:
            print("No food logged today.")
        else:
            for item in self.daily_log:
                print(f"- {item['quantity']}x {item['name']}: {item['calories']} kcal")
            print("---------------------")
            print(f"Total Calories: {total_calories} kcal")
            print(f"Total Protein: {total_protein:.1f}g")
            print(f"Total Carbs: {total_carbs:.1f}g")
            print(f"Total Fat: {total_fat:.1f}g")
        print("---------------------")

if __name__ == "__main__":
    counter = CalorieCounter()
    print("--- Simple CLI Calorie Counter ---")
    print("Commands: add <food_name> [quantity], summary, exit")
    print("Available foods: apple, banana, chicken breast, rice, egg")

    while True:
        command_input = input("> ").split(maxsplit=2)
        cmd = command_input[0].lower()

        if cmd == "add":
            if len(command_input) >= 2:
                food_name = command_input[1]
                quantity = int(command_input[2]) if len(command_input) == 3 else 1
                counter.add_food(food_name, quantity)
            else:
                print("Usage: add <food_name> [quantity]")
        elif cmd == "summary":
            counter.get_daily_summary()
        elif cmd == "exit":
            print("Exiting Calorie Counter.")
            break
        else:
            print("Unknown command.")