import sys

import pygame
from settings import FPS, GAME_NAME, HEIGHT, WIDTH


# Function Defintions
def update_lasers(lasers: list[pygame.Rect], deltaTime: float, speed: float = 300):
    for laser_rect in laser_list:
        # Temporary workaround until we can handle delta time based movement.
        laser_rect.y -= speed * deltaTime


def display_score():
    score_text = f"Score: {pygame.time.get_ticks() // 1000}"
    score_surface: pygame.Surface = font.render(score_text, True, "white")
    score_rect: pygame.Rect = score_surface.get_rect(midbottom=(WIDTH / 2, HEIGHT - 80))
    display_surface.blit(score_surface, score_rect)
    pygame.draw.rect(
        display_surface, "white", score_rect.inflate(30, 30), width=8, border_radius=5
    )


def can_shoot(duration=500) -> bool:
    current_time = pygame.time.get_ticks()
    if shoot_time < 0 or current_time - shoot_time > duration:
        return True

    return False


# Game Init
pygame.init()
pygame.display.set_caption(GAME_NAME)

display_surface: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
clock: pygame.Clock = pygame.time.Clock()

# Ship Import
ship_surface: pygame.Surface = pygame.image.load("../graphics/ship.png").convert_alpha()
ship_rect: pygame.Rect = ship_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))

# Laser Import + Definitions
laser_surface: pygame.Surface = pygame.image.load(
    "../graphics/laser.png"
).convert_alpha()
laser_list: list[pygame.Rect] = []
shoot_time = -1

# Background Import
background_surface: pygame.Surface = pygame.image.load(
    "../graphics/background.png"
).convert()

# Text Import
font: pygame.Font = pygame.font.Font("../graphics/subatomic.ttf", 50)


# Game Loop
while True:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot():
            laser_list.append(laser_surface.get_rect(midbottom=ship_rect.midtop))
            shoot_time = pygame.time.get_ticks()

    # Framerate Limiting
    dt: float = clock.tick(FPS) / 1000

    # Mouse Input
    ship_rect.center = pygame.mouse.get_pos()

    # Update
    update_lasers(laser_list, dt)
    laser_list = [laser for laser in laser_list if laser.bottom > 0]

    # Draw
    display_surface.fill("black")
    display_surface.blit(background_surface, (0, 0))
    display_score()
    display_surface.blit(ship_surface, ship_rect)
    for laser_rect in laser_list:
        display_surface.blit(laser_surface, laser_rect)

    pygame.display.update()
