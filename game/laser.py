import pygame
from pygame import Vector2


class Laser(pygame.sprite.Sprite):
    def __init__(self, position: Vector2, groups):
        super().__init__(groups)

        self.image = pygame.image.load("data/graphics/laser.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=position)
        self.pos = self.rect.topleft
        self.speed = 500.0
        self.direction = pygame.math.Vector2(0, -1)

    def update(self, deltaTime):
        self.pos += self.direction * self.speed * deltaTime
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))

    def is_on_screen(self) -> bool:
        return self.rect.y > 0
