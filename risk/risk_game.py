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

    def start_game(self):
        # This will contain the main game loop
        pass
