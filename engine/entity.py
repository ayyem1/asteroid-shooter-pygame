import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, imgPath: str, groups):
        super().__init__(groups)

        self.image = pygame.image.load(imgPath).convert_alpha()