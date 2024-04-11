import sys
import pygame
from settings import FPS, GAME_NAME, HEIGHT, WIDTH

# Game Init
pygame.init()
pygame.display.set_caption(GAME_NAME)

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Ship Import
ship_surface = pygame.image.load('../graphics/ship.png').convert_alpha()
ship_rect = ship_surface.get_rect(center = (WIDTH / 2, HEIGHT / 2))

# Laser Import
laser_surface = pygame.image.load('../graphics/laser.png').convert_alpha()
laser_rect = laser_surface.get_rect(midbottom = ship_rect.midtop)

# Background Import
background_surface = pygame.image.load('../graphics/background.png').convert()

# Text Import
font = pygame.font.Font('../graphics/subatomic.ttf', 50)
text_surface = font.render('Space', True, 'white')
text_rect = text_surface.get_rect(midbottom=(WIDTH / 2, HEIGHT - 80))


# Game Loop
while True:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Framerate Limiting
    clock.tick(FPS)

    # Mouse Input 
    ship_rect.center = pygame.mouse.get_pos()

    # Update
    laser_rect.y -= 10

    # Draw
    display_surface.fill('black')
    display_surface.blit(background_surface, (0,0))
    display_surface.blit(ship_surface, ship_rect)
    display_surface.blit(laser_surface, laser_rect)
    display_surface.blit(text_surface, text_rect)

    pygame.display.update()
        