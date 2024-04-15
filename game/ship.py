from typing import Union

import pygame
from pygame import Vector2

from engine.events import EventSystem
from game.game_events import GameEvents


class Ship(pygame.sprite.Sprite):
    def __init__(self, position: Vector2, laser_group: pygame.sprite.Group, groups):
        super().__init__(groups)

        self.image: pygame.Surface = pygame.image.load("data/graphics/ship.png")
        self.rect: pygame.Rect = self.image.get_rect(center=position)
        self.duration: float = 300.0
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

    def update(self, deltaTime):
        self.rect.center = pygame.mouse.get_pos()

        if self.can_shoot() and pygame.mouse.get_pressed()[0]:
            self.shoot()
