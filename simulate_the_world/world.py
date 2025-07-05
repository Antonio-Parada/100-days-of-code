import random

class Agent:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.energy = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.energy -= 1

    def interact(self, other_agent):
        # Simple interaction: exchange energy
        if self.energy > 10 and other_agent.energy < 90:
            self.energy -= 5
            other_agent.energy += 5
            print(f"{self.name} interacted with {other_agent.name}")

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.resources = {} # e.g., (x,y): amount

    def add_resource(self, x, y, amount):
        self.resources[(x, y)] = self.resources.get((x, y), 0) + amount

    def get_resource(self, x, y, amount):
        if self.resources.get((x, y), 0) >= amount:
            self.resources[(x, y)] -= amount
            return amount
        return 0

class World:
    def __init__(self, width, height):
        self.environment = Environment(width, height)
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def simulate_step(self):
        print("\n--- Simulating a step ---")
        # Agents move and interact
        for agent in self.agents:
            # Random movement
            dx = random.choice([-1, 0, 1])
            dy = random.choice([-1, 0, 1])
            agent.move(dx, dy)
            agent.x = max(0, min(agent.x, self.environment.width - 1))
            agent.y = max(0, min(agent.y, self.environment.height - 1))

            # Agent consumes resource
            consumed = self.environment.get_resource(agent.x, agent.y, 2)
            agent.energy += consumed

            # Agent interaction
            for other_agent in self.agents:
                if other_agent != agent and \
                   abs(agent.x - other_agent.x) <= 1 and \
                   abs(agent.y - other_agent.y) <= 1:
                    agent.interact(other_agent)

        # Regenerate some resources
        if random.random() < 0.5:
            res_x = random.randint(0, self.environment.width - 1)
            res_y = random.randint(0, self.environment.height - 1)
            self.environment.add_resource(res_x, res_y, 10)

    def print_status(self):
        print("\n--- World Status ---")
        print("Agents:")
        for agent in self.agents:
            print(f"  {agent.name}: Position=({agent.x}, {agent.y}), Energy={agent.energy}")
        print("Resources:")
        for (x, y), amount in self.environment.resources.items():
            if amount > 0:
                print(f"  ({x}, {y}): {amount}")

if __name__ == "__main__":
    world = World(width=10, height=10)
    world.add_agent(Agent("Alice", 0, 0))
    world.add_agent(Agent("Bob", 5, 5))
    world.environment.add_resource(2, 2, 50)

    for i in range(10):
        world.simulate_step()
        world.print_status()
