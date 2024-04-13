
import pygame
from pygame import Vector2


class Laser(pygame.sprite.Sprite):
    def __init__(self, position: Vector2, groups):
        super().__init__(groups)

        self.image = pygame.image.load("data/graphics/laser.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=position)