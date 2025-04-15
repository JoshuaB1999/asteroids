import pygame
from circleshape import CircleShape
from constants import *
from bullet import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.velocity = pygame.Vector2(0,0)
        self.acceleration = 300
        self.friction = 0.98

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)


    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()
        self.add_friction()
        self.position += self.velocity *dt

        if keys[pygame.K_a]:
            self.rotate((0-dt))
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move((0-dt))
        if keys[pygame.K_SPACE]:
            self.shoot(self.position.x, self.position.y, PLAYER_SHOOT_SPEED)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += forward * self.acceleration * dt

        if self.velocity.length() > PLAYER_SPEED:
            self.velocity.scale_to_length(PLAYER_SPEED)

    def add_friction(self):
        self.velocity *= self.friction

    def shoot(self, x, y, velocity):
        if self.timer > 0:
            pass
        else:
            shot = Shot(self.position.x, self.position.y, PLAYER_SHOOT_SPEED, self.rotation)
            shot.rotation = self.rotation
            self.timer = PLAYER_SHOOT_COOLDOWN
