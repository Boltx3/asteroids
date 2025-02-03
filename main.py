import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot
from constants import *

def main():
    drawable = pygame.sprite.Group()
    moveable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (drawable, moveable)
    Asteroid.containers = (asteroids, drawable, moveable)
    Shot.containers = (shots, moveable, drawable)
    AsteroidField.containers = moveable
    asteroid_field = AsteroidField()
    pygame.init()
    dt=0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        #close game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        moveable.update(dt)

        for asteroid in asteroids:
            if asteroid.collisions(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collisions(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()       
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
