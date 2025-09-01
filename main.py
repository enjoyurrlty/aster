import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    dt = 0
    
    Player.containers = (drawable, updatable)
    Shot.containers = (shots, drawable, updatable)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)


    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                sys.exit("Game over!")
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()
        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60.0) / 1000


if __name__ == "__main__":
    main()
