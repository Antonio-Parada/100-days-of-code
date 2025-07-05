import pygame
from engine import Vec2D, Particle, apply_gravity

# --- Pygame setup ---
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Physics Engine Simulation")
clock = pygame.time.Clock()

# --- Simulation setup ---
particles = [
    Particle(100, 100, mass=10),
    Particle(200, 150, mass=5),
    Particle(300, 200, mass=20),
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Update physics ---
    dt = clock.tick(60) / 1000.0  # Delta time in seconds
    for particle in particles:
        apply_gravity(particle)
        particle.update(dt)

        # Bounce off the floor
        if particle.position.y > height - 20:
            particle.position.y = height - 20
            particle.velocity.y *= -0.8  # Inelastic collision

    # --- Drawing ---
    screen.fill((20, 20, 40))  # Dark blue background
    for particle in particles:
        pygame.draw.circle(screen, (255, 255, 255), (int(particle.position.x), int(particle.position.y)), 10)

    pygame.display.flip()

pygame.quit()
