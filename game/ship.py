import pygame
from pygame import Vector2

from engine.entity import Entity


class Ship(Entity):
    def __init__(self, group, position: Vector2):
        super().__init__(imgPath="data/graphics/ship.png", group=group)

        self.rect = self.image.get_rect(center=position)
        self.duration: float = 500.0
        self.shoot_time: float = -1.0

    def can_shoot(self) -> bool:
        current_time = pygame.time.get_ticks()
        if self.shoot_time < 0 or current_time - self.shoot_time > self.duration:
            return True

        return False

    def shoot(self) -> bool:
        self.shoot_time = pygame.time.get_ticks()
