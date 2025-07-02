import random
import time
import os

class Agent:
    def __init__(self, x, y, char='A'):
        self.x = x
        self.y = y
        self.char = char

    def move(self, world_width, world_height):
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])
        self.x = max(0, min(world_width - 1, self.x + dx))
        self.y = max(0, min(world_height - 1, self.y + dy))

class WorldSimulator:
    def __init__(self, width=30, height=15, num_agents=5):
        self.width = width
        self.height = height
        self.agents = []
        for i in range(num_agents):
            self.agents.append(Agent(random.randint(0, width - 1), random.randint(0, height - 1), char=chr(ord('A') + i)))

    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _draw_world(self):
        self._clear_screen()
        grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]

        for agent in self.agents:
            grid[agent.y][agent.x] = agent.char

        for row in grid:
            print(''.join(row))

    def update(self):
        for agent in self.agents:
            agent.move(self.width, self.height)

    def run_simulation(self, steps=50):
        print("--- World Simulation ---")
        time.sleep(1)

        for _ in range(steps):
            self._draw_world()
            self.update()
            time.sleep(0.1)

        print("Simulation finished.")

if __name__ == '__main__':
    simulator = WorldSimulator()
    print("--- Interactive World Simulation ---")
    print("Agents move randomly. Press Ctrl+C to stop.")
    
    try:
        while True:
            simulator._draw_world()
            simulator.update()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Simulation stopped.")
    print("Simulation finished.")
