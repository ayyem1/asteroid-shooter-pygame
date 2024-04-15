import sys

import pygame

from engine.debug import display_fps
from engine.events import EventSystem
from game.game_events import GameEvents
from game.laser import Laser
from game.settings import FPS, GAME_NAME, WINDOW_HEIGHT, WINDOW_WIDTH
from game.ship import Ship


class Game:
    def __init__(self) -> None:
        # Init pygame
        pygame.init()

        # Init window
        pygame.display.set_caption(GAME_NAME)
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        # Init clock
        self.clock = pygame.time.Clock()

        # Init events
        for event_type in GameEvents:
            EventSystem().create_custom_event(custom_event_type=event_type)

        # Init game components
        self.spaceship_group = pygame.sprite.GroupSingle()
        self.ship = Ship(
            position=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2),
            laser_group=self.laser_group,
            groups=self.spaceship_group,
        )

        self.laser_group = pygame.sprite.Group()
        self.background_surface = pygame.image.load("data/graphics/background.png")

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == EventSystem().user_event_slot:
                    if event.custom_event_type == GameEvents.PLAYER_PRIMARY_SHOOT:
                        Laser(
                            position=self.ship.rect.midtop,
                            groups=self.laser_group,
                        )

            dt: float = self.clock.tick(FPS) / 1000.0

            self.spaceship_group.update(deltaTime=dt)
            self.laser_group.update(deltaTime=dt)

            for laser in self.laser_group:
                if not laser.is_on_screen():
                    self.laser_group.remove(laser)

            self.display_surface.fill("black")
            self.display_surface.blit(self.background_surface, (0, 0))

            display_fps(self.clock, WINDOW_WIDTH)
            self.laser_group.draw(self.display_surface)
            self.spaceship_group.draw(self.display_surface)

            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
