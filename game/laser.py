import pygame
from pygame import Vector2

from game.settings import LASER_SPEED


class Laser(pygame.sprite.Sprite):
    def __init__(self, position: Vector2, groups: pygame.sprite.Group):
        super().__init__(groups)

        # Todo: Optimize this. We load this image each time we spawn a laser.
        self.image = pygame.image.load("data/graphics/laser.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=position)
        self.pos = self.rect.topleft
        self.speed = LASER_SPEED
        self.direction = pygame.math.Vector2(0, -1)

    def update(self, delta_time: float):
        self.pos += self.direction * self.speed * delta_time
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))

    def is_on_screen(self) -> bool:
        return self.rect.y > 0
