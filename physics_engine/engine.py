import math

class Vec2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vec2D(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vec2D(self.x / scalar, self.y / scalar)

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vec2D(0, 0)
        return self / mag

class Particle:
    def __init__(self, x, y, mass=1.0):
        self.position = Vec2D(x, y)
        self.velocity = Vec2D(0, 0)
        self.acceleration = Vec2D(0, 0)
        self.mass = mass

    def apply_force(self, force):
        self.acceleration += force / self.mass

    def update(self, dt):
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt
        self.acceleration = Vec2D(0, 0)  # Reset acceleration after each update

def apply_gravity(particle, gravity=Vec2D(0, 9.81)):
    particle.apply_force(gravity * particle.mass)
