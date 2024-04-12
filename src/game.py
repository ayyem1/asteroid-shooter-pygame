import sys

import pygame
from debug import display_fps
from settings import FPS, GAME_NAME, HEIGHT, WIDTH


class Game:
    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption(GAME_NAME)

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.clock.tick(FPS)

            self.screen.fill("black")
            display_fps(self.clock)

            pygame.display.update()
