import sys

import pygame

from engine.debug import display_fps
from engine.entity import Entity
from game.settings import FPS, GAME_NAME, WINDOW_HEIGHT, WINDOW_WIDTH


class Game:
    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption(GAME_NAME)

        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

        self.spaceship_group = pygame.sprite.Group()
        self.ship = Entity(
            imgPath="data/graphics/ship.png",
            group=self.spaceship_group,
            position=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2),
        )

        self.laser_group = pygame.sprite.Group()
        self.laser_list: list[pygame.Rect] = []
        self.shoot_time: float = -1

        self.background_surface = pygame.image.load("data/graphics/background.png")

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and self.can_shoot():
                    self.laser_list.append(
                        Entity(
                            imgPath="data/graphics/laser.png",
                            group=self.laser_group,
                            position=self.ship.rect.midtop,
                        )
                    )
                    self.shoot_time = pygame.time.get_ticks()

            self.clock.tick(FPS)

            self.ship.rect.center = pygame.mouse.get_pos()

            self.display_surface.fill("black")
            self.display_surface.blit(self.background_surface, (0, 0))

            display_fps(self.clock, WINDOW_WIDTH)
            self.spaceship_group.draw(self.display_surface)
            self.laser_group.draw(self.display_surface)

            pygame.display.update()

    def can_shoot(self, duration: float = 500) -> bool:
        current_time = pygame.time.get_ticks()
        if self.shoot_time < 0 or current_time - self.shoot_time > duration:
            return True

        return False


if __name__ == "__main__":
    game = Game()
    game.run()
