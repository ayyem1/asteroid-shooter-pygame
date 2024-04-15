from random import randint, uniform

import pygame

from game.settings import METEOR_SPEED_RANGE, WINDOW_HEIGHT, WINDOW_WIDTH


class Meteor(pygame.sprite.Sprite):
    def __init__(self, groups: pygame.sprite.Group):
        super().__init__(groups)

        # Todo: Optimize this. We load this image each time we spawn a laser.
        self.image = pygame.image.load("data/graphics/meteor.png").convert_alpha()

        x_pos: float = randint(-100, WINDOW_WIDTH + 100)
        y_pos: float = randint(-150, -50)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))
        self.pos = self.rect.topleft

        lower, upper = METEOR_SPEED_RANGE
        self.speed = randint(lower, upper)
        self.direction = pygame.math.Vector2(uniform(-0.5, 0.5), 1)

    def update(self, deltaTime):
        self.pos += self.direction * self.speed * deltaTime
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))

    def is_on_screen(self) -> bool:
        return self.rect.y < WINDOW_HEIGHT
