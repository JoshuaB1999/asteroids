# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import *
from asteroidfield import *

updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
asteroidfield = pygame.sprite.Group()
bullets = pygame.sprite.Group()
AsteroidField.containers = (updateable,)
Player.containers = (updateable, drawable)
Asteroid.containers = (asteroids, updateable, drawable)
Shot.containers = (bullets, updateable, drawable)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    playerchar = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    score = 0

    asteroid_field = AsteroidField()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f"Your Score is {score}!")
                return
        screen.fill((0,0,0))
        updateable.update(dt)
        for asteroid in asteroids:
            for bullet in bullets:
                if bullet.collision(asteroid):
                    score += 1
                    asteroid.split()
                    bullet.kill()
            if playerchar.collision(asteroid):
                print("Game Over!")
                print(f"Your Score is {score}!")
                sys.exit()
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
