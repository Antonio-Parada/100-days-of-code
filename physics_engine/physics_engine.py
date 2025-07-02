import math
import time
import os

class Particle:
    def __init__(self, x, y, radius, mass, vx=0, vy=0, color='o'):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.vx = vx
        self.vy = vy
        self.color = color

    def apply_force(self, fx, fy, dt):
        self.vx += (fx / self.mass) * dt
        self.vy += (fy / self.mass) * dt

    def update_position(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

class PhysicsEngine:
    def __init__(self, width, height, gravity=9.8, dt=0.1):
        self.width = width
        self.height = height
        self.gravity = gravity
        self.dt = dt # Time step
        self.particles = []

    def add_particle(self, particle):
        self.particles.append(particle)

    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _draw_simulation(self):
        self._clear_screen()
        grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]

        for particle in self.particles:
            px = int(particle.x)
            py = int(particle.y)
            if 0 <= px < self.width and 0 <= py < self.height:
                grid[py][px] = particle.color

        for row in grid:
            print(''.join(row))

    def update(self):
        for particle in self.particles:
            # Apply gravity
            particle.apply_force(0, particle.mass * self.gravity, self.dt)

            # Update position
            particle.update_position(self.dt)

            # Basic wall collision (bounce)
            if particle.x - particle.radius < 0:
                particle.x = particle.radius
                particle.vx *= -0.8 # Bounce with some energy loss
            if particle.x + particle.radius > self.width:
                particle.x = self.width - particle.radius
                particle.vx *= -0.8
            if particle.y - particle.radius < 0:
                particle.y = particle.radius
                particle.vy *= -0.8
            if particle.y + particle.radius > self.height:
                particle.y = self.height - particle.radius
                particle.vy *= -0.8

    def run_simulation(self, duration):
        start_time = time.time()
        while time.time() - start_time < duration:
            self.update()
            self._draw_simulation()
            time.sleep(self.dt)

if __name__ == '__main__':
    engine = PhysicsEngine(width=40, height=20, dt=0.05)
    
    # Example: A single particle falling
    particle = Particle(x=5, y=0, radius=0, mass=1, color='@')
    engine.add_particle(particle)

    print("Running simulation for 10 seconds...")
    engine.run_simulation(duration=10)
    print("Simulation finished.")