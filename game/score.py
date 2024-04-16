import pygame

from game.settings import WINDOW_WIDTH


class Score:
    def __init__(self) -> None:
        self.font: pygame.Font = pygame.font.Font("data/graphics/subatomic.ttf", 30)

    def display(self):
        score_text = f"Score: {pygame.time.get_ticks() // 1000}"
        score_surface: pygame.Surface = self.font.render(score_text, True, "white")
        score_rect: pygame.Rect = score_surface.get_rect(midtop=(WINDOW_WIDTH / 2, 20))
        display_surface = pygame.display.get_surface()
        display_surface.blit(score_surface, score_rect)
        pygame.draw.rect(
            display_surface,
            "white",
            score_rect.inflate(30, 30),
            width=4,
            border_radius=3,
        )
