import sys
from random import randint, uniform

import pygame

from game.settings import FPS, GAME_NAME, WINDOW_HEIGHT, WINDOW_WIDTH


# Function Defintions
def update_lasers(lasers: list[pygame.Rect], deltaTime: float, speed: float = 300):
    for laser_rect in lasers:
        # Temporary workaround until we can handle delta time based movement.
        laser_rect.y -= speed * deltaTime


def update_meteors(
    meteors: list[tuple[pygame.Rect, pygame.Vector2]],
    deltaTime: float,
    speed: float = 300,
):
    for meteor_tuple in meteors:
        # Temporary workaround until we can handle delta time based movement.
        meteor_rect = meteor_tuple[0]
        direction = meteor_tuple[1]
        meteor_rect.center += direction * speed * deltaTime


def display_score():
    score_text = f"Score: {pygame.time.get_ticks() // 1000}"
    score_surface: pygame.Surface = font.render(score_text, True, "white")
    score_rect: pygame.Rect = score_surface.get_rect(
        midbottom=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80)
    )
    display_surface.blit(score_surface, score_rect)
    pygame.draw.rect(
        display_surface, "white", score_rect.inflate(30, 30), width=8, border_radius=5
    )


def display_fps():
    fps_text = "{:.2f}".format(clock.get_fps())
    fps_surface: pygame.Surface = font.render(fps_text, True, "white")
    fps_rect: pygame.Rect = fps_surface.get_rect(midbottom=(WINDOW_WIDTH - 100, 80))
    display_surface.blit(fps_surface, fps_rect)
    pygame.draw.rect(
        display_surface, "white", fps_rect.inflate(30, 30), width=8, border_radius=5
    )


def can_shoot(duration=500) -> bool:
    current_time = pygame.time.get_ticks()
    if shoot_time < 0 or current_time - shoot_time > duration:
        return True

    return False


def quit_game():
    pygame.quit()
    sys.exit()


# Game Init
pygame.init()
pygame.display.set_caption(GAME_NAME)

display_surface: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock: pygame.Clock = pygame.time.Clock()

# Ship Import
ship_surface: pygame.Surface = pygame.image.load("../graphics/ship.png").convert_alpha()
ship_rect: pygame.Rect = ship_surface.get_rect(
    center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
)

# Laser Import + Definitions
laser_surface: pygame.Surface = pygame.image.load(
    "../graphics/laser.png"
).convert_alpha()
laser_list: list[pygame.Rect] = []
shoot_time = -1

# Meteor Import + Definitions
meteor_surface: pygame.Surface = pygame.image.load(
    "../graphics/meteor.png"
).convert_alpha()
meteor_list: list[tuple[pygame.Rect, pygame.Vector2]] = []
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 500)

# Background Import
background_surface: pygame.Surface = pygame.image.load(
    "../graphics/background.png"
).convert()

# Text Import
font: pygame.Font = pygame.font.Font("../graphics/subatomic.ttf", 50)

# Audio Import
laser_shoot_sound = pygame.mixer.Sound("../sounds/laser.ogg")
explosion_sound = pygame.mixer.Sound("../sounds/explosion.wav")
background_music = pygame.mixer.Sound("../sounds/music.wav")
background_music.play(loops=-1)

# Game Loop
while True:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot():
            laser_list.append(laser_surface.get_rect(midbottom=ship_rect.midtop))
            shoot_time = pygame.time.get_ticks()
            laser_shoot_sound.play()
        if event.type == meteor_timer:
            x_pos = randint(-100, WINDOW_WIDTH + 100)
            y_pos = randint(-150, -50)
            meteor_rect = meteor_surface.get_rect(center=(x_pos, y_pos))
            direction = pygame.math.Vector2(uniform(-0.5, 0.5), 1)
            meteor_list.append((meteor_rect, direction))

    # Framerate Limiting
    dt: float = clock.tick(FPS) / 1000

    # Mouse Input
    ship_rect.center = pygame.mouse.get_pos()

    # Update
    update_lasers(laser_list, dt)
    laser_list = [laser for laser in laser_list if laser.bottom > 0]

    update_meteors(meteor_list, dt)
    meteor_list = [
        meteor_tuple
        for meteor_tuple in meteor_list
        if meteor_tuple[0].top < WINDOW_HEIGHT
    ]
    for meteor in meteor_list:
        if ship_rect.colliderect(meteor[0]):
            quit_game()

        for laser in laser_list:
            if laser.colliderect(meteor[0]):
                explosion_sound.play()
                meteor_list.remove(meteor)
                laser_list.remove(laser)

    # Draw
    display_surface.fill("black")
    display_surface.blit(background_surface, (0, 0))
    display_score()
    display_fps()
    display_surface.blit(ship_surface, ship_rect)
    for laser_rect in laser_list:
        display_surface.blit(laser_surface, laser_rect)

    for meteor_tuple in meteor_list:
        display_surface.blit(meteor_surface, meteor_tuple[0])

    pygame.display.update()
