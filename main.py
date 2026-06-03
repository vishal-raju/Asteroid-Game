import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, drawable ,updatable)

    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()

    Shot.containers = (shots, drawable, updatable)

    

    while True:

        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        for each_draw in drawable:
            each_draw.draw(screen)
        
        updatable.update(dt)

        for asteroid_obj in asteroids:
            if player.collides_with(asteroid_obj):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()



