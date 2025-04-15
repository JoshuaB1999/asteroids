import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, velocity_magnitude, rotation):
        CircleShape.__init__(self, x, y, SHOT_RADIUS)
        self.rotation = rotation
        self.velocity = pygame.Vector2(0 ,1).rotate(self.rotation) * velocity_magnitude

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), SHOT_RADIUS)
    def update(self, dt):
        self.position += self.velocity * dt
