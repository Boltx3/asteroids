import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    #Draw Method
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position, self.radius,2)

    #Update Method from circleshape
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        #randomize angles on collision
        random_angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        #Create new asteroids
        #Change velocity and direction
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = vector1 * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = vector2 * 1.2


