from random import randint, uniform

import pygame

from game.settings import METEOR_SPEED_RANGE, WINDOW_HEIGHT, WINDOW_WIDTH


class Meteor(pygame.sprite.Sprite):
    def __init__(self, groups: pygame.sprite.Group):
        super().__init__(groups)

        # Todo: Optimize this. We load this image each time we spawn a laser.
        meteor_surface: pygame.Surface = pygame.image.load(
            "data/graphics/meteor.png"
        ).convert_alpha()
        scale_factor: float = uniform(0.5, 1.5)
        self.original_image: pygame.Surface = pygame.transform.scale_by(
            meteor_surface, (scale_factor, scale_factor)
        )
        self.image: pygame.Surface = self.original_image

        x_pos: float = randint(-100, WINDOW_WIDTH + 100)
        y_pos: float = randint(-150, -50)
        self.rect: pygame.Rect = self.image.get_rect(center=(x_pos, y_pos))
        self.pos: pygame.Vector2 = self.rect.topleft

        lower, upper = METEOR_SPEED_RANGE
        self.speed = randint(lower, upper)
        self.direction = pygame.math.Vector2(uniform(-0.5, 0.5), 1)

        self.rotation = 0
        self.rotation_speed = randint(20, 50)

    def rotate(self, delta_time: float):
        self.rotation += self.rotation_speed * delta_time
        rotated_surface = pygame.transform.rotozoom(
            self.original_image, self.rotation, 1
        )
        self.image = rotated_surface
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self, delta_time: float):
        self.pos += self.direction * self.speed * delta_time
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        self.rotate(delta_time=delta_time)

    def is_on_screen(self) -> bool:
        return self.rect.y < WINDOW_HEIGHT
