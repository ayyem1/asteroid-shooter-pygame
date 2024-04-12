import pygame
from settings import WIDTH

pygame.init()
debug_font = pygame.font.Font(None, 30)


def log_debug(info, y=10, x=10):
    display_surface = pygame.display.get_surface()
    debug_surf = debug_font.render(str(info), True, "white")
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    pygame.draw.rect(display_surface, "black", debug_rect)
    display_surface.blit(debug_surf, debug_rect)


def display_fps(clock: pygame.Clock):
    display_surface = pygame.display.get_surface()
    fps_text = "{:.2f}".format(clock.get_fps())
    fps_surface: pygame.Surface = debug_font.render(fps_text, True, "white")
    fps_rect: pygame.Rect = fps_surface.get_rect(midbottom=(WIDTH - 100, 80))
    display_surface.blit(fps_surface, fps_rect)
    pygame.draw.rect(
        display_surface, "white", fps_rect.inflate(30, 30), width=4, border_radius=5
    )
