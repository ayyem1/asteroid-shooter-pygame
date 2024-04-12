import sys

import pygame

from engine.debug import display_fps
from game.settings import FPS, GAME_NAME, WINDOW_HEIGHT, WINDOW_WIDTH


class Game:
    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption(GAME_NAME)

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.clock.tick(FPS)

            self.screen.fill("black")
            display_fps(self.clock, WINDOW_WIDTH)

            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
