class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.territories = []
        self.armies = 0

class Territory:
    def __init__(self, name, continent):
        self.name = name
        self.continent = continent
        self.owner = None
        self.armies = 0
        self.neighbors = []

class Game:
    def __init__(self):
        self.players = []
        self.territories = {}
        self.continents = {}

    def add_player(self, player):
        self.players.append(player)

    def add_territory(self, territory):
        self.territories[territory.name] = territory

    def add_continent(self, name, bonus_armies):
        self.continents[name] = {"bonus_armies": bonus_armies, "territories": []}

    def add_territory_to_continent(self, territory_name, continent_name):
        if continent_name in self.continents and territory_name in self.territories:
            self.continents[continent_name]["territories"].append(territory_name)

    def _initialize_map(self):
        # Define Continents
        self.add_continent("North America", 5)

        # Define Territories
        alaska = Territory("Alaska", "North America")
        nw_territory = Territory("Northwest Territory", "North America")
        greenland = Territory("Greenland", "North America")
        alberta = Territory("Alberta", "North America")
        ontario = Territory("Ontario", "North America")
        quebec = Territory("Quebec", "North America")
        w_united_states = Territory("Western United States", "North America")
        e_united_states = Territory("Eastern United States", "North America")
        central_america = Territory("Central America", "North America")

        self.add_territory(alaska)
        self.add_territory(nw_territory)
        self.add_territory(greenland)
        self.add_territory(alberta)
        self.add_territory(ontario)
        self.add_territory(quebec)
        self.add_territory(w_united_states)
        self.add_territory(e_united_states)
        self.add_territory(central_america)

        # Add territories to continents
        self.add_territory_to_continent("Alaska", "North America")
        self.add_territory_to_continent("Northwest Territory", "North America")
        self.add_territory_to_continent("Greenland", "North America")
        self.add_territory_to_continent("Alberta", "North America")
        self.add_territory_to_continent("Ontario", "North America")
        self.add_territory_to_continent("Quebec", "North America")
        self.add_territory_to_continent("Western United States", "North America")
        self.add_territory_to_continent("Eastern United States", "North America")
        self.add_territory_to_continent("Central America", "North America")

        # Define Neighbors
        alaska.neighbors = [nw_territory, alberta, "Kamchatka"]
        nw_territory.neighbors = [alaska, alberta, ontario, greenland]
        greenland.neighbors = [nw_territory, ontario, quebec, "Iceland"]
        alberta.neighbors = [alaska, nw_territory, ontario, w_united_states]
        ontario.neighbors = [nw_territory, alberta, w_united_states, e_united_states, quebec, greenland]
        quebec.neighbors = [ontario, greenland, e_united_states]
        w_united_states.neighbors = [alberta, ontario, e_united_states, central_america]
        e_united_states.neighbors = [w_united_states, ontario, quebec, central_america]
        central_america.neighbors = [w_united_states, e_united_states, "Venezuela"]

    def calculate_reinforcements(self, player):
        # Base reinforcements from territories
        reinforcements = max(3, len(player.territories) // 3)

        # Continent bonuses
        for continent_name, continent_data in self.continents.items():
            if all(self.territories[t].owner == player for t in continent_data["territories"]):
                reinforcements += continent_data["bonus_armies"]
        return reinforcements

    def setup_game(self):
        self._initialize_map()

        # Setup Players
        player1 = Player("Player 1", "Red")
        player2 = Player("Player 2", "Blue")
        self.add_player(player1)
        self.add_player(player2)

        # Distribute Territories randomly
        import random
        territory_names = list(self.territories.keys())
        random.shuffle(territory_names)

        for i, territory_name in enumerate(territory_names):
            owner = self.players[i % len(self.players)]
            territory = self.territories[territory_name]
            territory.owner = owner
            owner.territories.append(territory)
            territory.armies = 1 # Each territory starts with 1 army
            owner.armies += 1 # Count initial armies for player

        # Distribute initial armies (simplified for now)
        # Each player gets a base number of armies plus armies for territories
        initial_armies_per_player = 30 # Example base
        for player in self.players:
            player.armies = initial_armies_per_player - len(player.territories) + player.armies # Adjust for initial territory armies

    def display_game_state(self):
        print("\n--- Current Game State ---")
        for player in self.players:
            print(f"\nPlayer: {player.name} ({player.color}) - Armies: {player.armies}")
            for territory in player.territories:
                print(f"  - {territory.name} ({territory.armies} armies)")

    def start_game(self):
        print("Game Started!")
        self.setup_game()
        self.display_game_state()

        # Simple game loop for demonstration
        turn = 1
        while True:
            print(f"\n--- Turn {turn} ---")
            for player in self.players:
                print(f"\n{player.name}'s turn.")
                reinforcements = self.calculate_reinforcements(player)
                player.armies += reinforcements
                print(f"{player.name} receives {reinforcements} reinforcements. Total armies: {player.armies}")
                # For now, just place all reinforcements on a random territory
                if player.territories:
                    random_territory = random.choice(player.territories)
                    random_territory.armies += reinforcements
                    print(f"Placed {reinforcements} armies on {random_territory.name}.")
                self.display_game_state()

                # Placeholder for attack and fortification phases
                # input("Press Enter to continue to next phase...")

                # Attack Phase (Simplified)
                print("\n--- Attack Phase ---")
                # For demonstration, let's assume a simple attack scenario
                # In a real game, players would choose attacking and defending territories
                # and roll dice.
                # For now, let's just simulate a single attack if possible.
                
                # Find an attacking territory and a neighboring enemy territory
                attacking_territory = None
                defending_territory = None
                
                for t in player.territories:
                    for neighbor_name in t.neighbors:
                        if neighbor_name in self.territories:
                            neighbor_territory = self.territories[neighbor_name]
                            if neighbor_territory.owner != player:
                                attacking_territory = t
                                defending_territory = neighbor_territory
                                break
                    if attacking_territory:
                        break

                if attacking_territory and defending_territory:
                    print(f"{player.name} ({attacking_territory.name}) attacks {defending_territory.owner.name} ({defending_territory.name})")
                    # Simple attack logic: attacker wins if they have more armies
                    if attacking_territory.armies > defending_territory.armies:
                        print(f"{player.name} wins the attack!")
                        # Move armies to conquered territory (simplified)
                        attacking_territory.armies -= 1 # Leave one army behind
                        defending_territory.owner.territories.remove(defending_territory)
                        defending_territory.owner.armies -= defending_territory.armies
                        
                        defending_territory.owner = player
                        player.territories.append(defending_territory)
                        player.armies += defending_territory.armies
                        defending_territory.armies = 1 # Occupy with 1 army
                        attacking_territory.armies -= 1 # Move one army from attacking to defending
                        print(f"{player.name} now owns {defending_territory.name}.")
                    else:
                        print(f"{defending_territory.owner.name} defends successfully!")
                        attacking_territory.armies -= 1 # Attacker loses one army
                else:
                    print("No valid attack possible for this player in this turn (simplified).")

                self.display_game_state()

                # Fortification Phase (Simplified)
                print("\n--- Fortification Phase ---")
                # For now, let's assume a simple fortification scenario
                # Player can move armies from one of their territories to an adjacent owned territory.
                
                # Find a territory to fortify from and to
                from_territory = None
                to_territory = None

                for t_from in player.territories:
                    if t_from.armies > 1: # Must have at least 2 armies to move 1
                        for neighbor_name in t_from.neighbors:
                            if neighbor_name in self.territories:
                                t_to = self.territories[neighbor_name]
                                if t_to.owner == player: # Must be owned by the same player
                                    from_territory = t_from
                                    to_territory = t_to
                                    break
                        if from_territory:
                            break
                
                if from_territory and to_territory:
                    print(f"{player.name} fortifies from {from_territory.name} to {to_territory.name}")
                    from_territory.armies -= 1
                    to_territory.armies += 1
                    print(f"Moved 1 army from {from_territory.name} to {to_territory.name}.")
                else:
                    print("No valid fortification possible for this player in this turn (simplified).")

                self.display_game_state()

                # Check for win condition
                winner = self.check_win_condition()
                if winner:
                    print(f"
!!! {winner.name} has conquered all territories and won the game !!!")
                    break

            turn += 1
            if turn > 3: # Limit turns for demonstration
                break
        print("Game Over (Demo End).")

    def check_win_condition(self):
        for player in self.players:
            if len(player.territories) == len(self.territories):
                return player
        return None
