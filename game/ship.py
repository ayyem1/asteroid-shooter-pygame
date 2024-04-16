from typing import Union

import pygame
from pygame import Vector2

from engine.events import EventSystem
from game.game_events import GameEvents
from game.settings import SHIP_SHOOT_COOLDOWN


class Ship(pygame.sprite.Sprite):
    def __init__(self, position: Vector2, groups: pygame.sprite.Group):
        super().__init__(groups)

        self.image: pygame.Surface = pygame.image.load("data/graphics/ship.png")
        self.rect: pygame.Rect = self.image.get_rect(center=position)
        self.duration: float = SHIP_SHOOT_COOLDOWN
        self.shoot_time: float = -1.0
        self.player_shoot_event: Union[
            pygame.Event, None
        ] = EventSystem().get_custom_event(
            custom_event_type=GameEvents.PLAYER_PRIMARY_SHOOT
        )

    def can_shoot(self) -> bool:
        current_time = pygame.time.get_ticks()
        if self.shoot_time < 0 or current_time - self.shoot_time > self.duration:
            return True

        return False

    def shoot(self) -> bool:
        if self.player_shoot_event:
            pygame.event.post(self.player_shoot_event)

        self.shoot_time = pygame.time.get_ticks()

    def meteor_collision(self, meteor_group: pygame.sprite.Group):
        if pygame.sprite.spritecollide(self, meteor_group, True):
            pygame.event.post(
                EventSystem().get_custom_event(
                    custom_event_type=GameEvents.SHIP_DESTROYED
                )
            )

    def update(self, delta_time: float, meteor_group: pygame.sprite.Group):
        self.rect.center = pygame.mouse.get_pos()

        if self.can_shoot() and pygame.mouse.get_pressed()[0]:
            self.shoot()

        self.meteor_collision(meteor_group=meteor_group)
