import sys
import pygame
from settings import FPS, GAME_NAME, HEIGHT, WIDTH

pygame.init()
pygame.display.set_caption(GAME_NAME)

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

ship_surface = pygame.image.load('../graphics/ship.png').convert_alpha()
ship_rect = ship_surface.get_rect(center = (WIDTH / 2, HEIGHT / 2))

background_surface = pygame.image.load('../graphics/background.png').convert()

font = pygame.font.Font('../graphics/subatomic.ttf', 50)
text_surface = font.render('Space', True, 'white')
text_rect = text_surface.get_rect(midbottom=(WIDTH / 2, HEIGHT - 80))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    display_surface.fill('black')
    display_surface.blit(background_surface, (0,0))

    if (ship_rect.y > 0):
        ship_rect.y -= 4

    display_surface.blit(ship_surface, ship_rect)
    display_surface.blit(text_surface, text_rect)

    pygame.display.update()
    clock.tick(FPS)
        