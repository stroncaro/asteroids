import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color("white"), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        angle = random.uniform(20, 50)
        new_velocities = (self.velocity.rotate(angle), self.velocity.rotate(-angle))
        for velocity in new_velocities:
            new_asteroid = Asteroid(*self.position, new_radius)
            new_asteroid.velocity = velocity * 1.2
