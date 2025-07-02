import random

class SimpleRiskGame:
    def __init__(self):
        print("--- Simple CLI Risk Game Simulation ---")
        print("This script simulates basic combat in Risk using dice rolls.")

    def roll_dice(self, num_dice):
        rolls = [random.randint(1, 6) for _ in range(num_dice)]
        rolls.sort(reverse=True) # Sort for easier comparison in combat
        return rolls

    def simulate_combat(self, attacking_armies, defending_armies):
        print(f"\nCombat Simulation: {attacking_armies} attackers vs. {defending_armies} defenders")
        
        attacker_losses = 0
        defender_losses = 0

        # Attacker rolls up to 3 dice, defender up to 2
        num_attacker_dice = min(attacking_armies - 1, 3) # Must leave at least one army behind
        num_defender_dice = min(defending_armies, 2)

        if num_attacker_dice <= 0 or num_defender_dice <= 0:
            print("Not enough armies for combat.")
            return attacking_armies, defending_armies

        attacker_rolls = self.roll_dice(num_attacker_dice)
        defender_rolls = self.roll_dice(num_defender_dice)

        print(f"Attacker rolls: {attacker_rolls}")
        print(f"Defender rolls: {defender_rolls}")

        # Compare dice rolls
        for i in range(min(len(attacker_rolls), len(defender_rolls))):
            if attacker_rolls[i] > defender_rolls[i]:
                defender_losses += 1
            else:
                attacker_losses += 1
        
        print(f"Attacker losses: {attacker_losses}, Defender losses: {defender_losses}")
        return attacking_armies - attacker_losses, defending_armies - defender_losses

if __name__ == "__main__":
    game = SimpleRiskGame()

    while True:
        try:
            attacker_armies = int(input("Enter number of attacking armies (min 2, type 0 to exit): "))
            if attacker_armies == 0:
                print("Exiting game.")
                break
            if attacker_armies < 2:
                print("Attacker must have at least 2 armies.")
                continue

            defender_armies = int(input("Enter number of defending armies (min 1): "))
            if defender_armies < 1:
                print("Defender must have at least 1 army.")
                continue

            remaining_attackers, remaining_defenders = game.simulate_combat(attacker_armies, defender_armies)
            print(f"Remaining Attackers: {remaining_attackers}, Remaining Defenders: {remaining_defenders}")

        except ValueError:
            print("Invalid input. Please enter a number.")
