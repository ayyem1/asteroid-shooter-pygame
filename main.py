import sys

import pygame

from engine.debug import display_fps
from game.laser import Laser
from game.settings import FPS, GAME_NAME, WINDOW_HEIGHT, WINDOW_WIDTH
from game.ship import Ship


class Game:
    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption(GAME_NAME)

        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

        self.spaceship_group = pygame.sprite.GroupSingle()
        self.ship = Ship(
            position=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2),
            groups=self.spaceship_group,
        )

        self.laser_group = pygame.sprite.Group()
        self.laser_list: list[pygame.Rect] = []

        self.background_surface = pygame.image.load("data/graphics/background.png")

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and self.ship.can_shoot():
                    # TODO: We create a surface and load the img each time this entity is created
                    self.laser_list.append(
                        Laser(
                            position=self.ship.rect.midtop,
                            groups=self.laser_group,
                        )
                    )
                    self.ship.shoot()

            self.clock.tick(FPS)

            self.ship.rect.center = pygame.mouse.get_pos()

            self.display_surface.fill("black")
            self.display_surface.blit(self.background_surface, (0, 0))

            display_fps(self.clock, WINDOW_WIDTH)
            self.laser_group.draw(self.display_surface)
            self.spaceship_group.draw(self.display_surface)

            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
