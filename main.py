import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from constants import *

def main():
    drawable = pygame.sprite.Group()
    moveable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    Player.containers = (drawable, moveable)
    Asteroid.containers = (asteroid, drawable, moveable)
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
        screen.fill("black")
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()       
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
