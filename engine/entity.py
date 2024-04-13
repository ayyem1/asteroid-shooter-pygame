import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, imgPath: str, group: pygame.sprite.Group):
        super().__init__(group)

        self.image = pygame.image.load(imgPath).convert_alpha()