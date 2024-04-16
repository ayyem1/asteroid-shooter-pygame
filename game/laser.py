import pygame
from pygame import Vector2

from engine.events import EventSystem
from game.game_events import GameEvents
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

    def meteor_collision(self, meteor_group: pygame.sprite.Group):
        if pygame.sprite.spritecollide(self, meteor_group, True):
            e = EventSystem().get_custom_event(
                custom_event_type=GameEvents.METEOR_DESTROYED
            )
            e.laser = self
            pygame.event.post(e)

    def update(self, delta_time: float, meteor_group: pygame.sprite.Group):
        self.pos += self.direction * self.speed * delta_time
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))

        if self.rect.y < 0:
            self.kill()
        else:
            self.meteor_collision(meteor_group=meteor_group)
