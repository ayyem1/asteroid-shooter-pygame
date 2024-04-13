
from pygame import Vector2

from engine.entity import Entity


class Laser(Entity):
    def __init__(self, group, position: Vector2):
        super().__init__(imgPath="data/graphics/laser.png", group=group)

        self.rect = self.image.get_rect(midbottom=position)