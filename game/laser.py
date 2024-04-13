
from pygame import Vector2

from engine.entity import Entity


class Laser(Entity):
    def __init__(self, position: Vector2, groups):
        super().__init__(imgPath="data/graphics/laser.png", groups=groups)

        self.rect = self.image.get_rect(midbottom=position)