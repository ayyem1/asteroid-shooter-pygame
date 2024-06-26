import sys

import pygame

from engine.debug import display_fps
from engine.events import EventSystem
from game.game_events import GameEvents
from game.laser import Laser
from game.meteor import Meteor
from game.score import Score
from game.settings import FPS, GAME_NAME, METEOR_SPAWN_RATE, WINDOW_HEIGHT, WINDOW_WIDTH
from game.ship import Ship


class Game:
    def __init__(self) -> None:
        # Init pygame
        pygame.init()

        # Init window
        pygame.display.set_caption(GAME_NAME)
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        # Init clock
        self.clock = pygame.time.Clock()

        # Init events
        for event_type in GameEvents:
            EventSystem().create_custom_event(custom_event_type=event_type)

        # Init game components
        self.spaceship_group = pygame.sprite.GroupSingle()
        self.ship = Ship(
            position=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2),
            groups=self.spaceship_group,
        )
        self.meteor_timer = pygame.time.set_timer(
            EventSystem().get_custom_event(
                custom_event_type=GameEvents.METEOR_TIMER_COMPLETE
            ),
            METEOR_SPAWN_RATE,
        )

        self.laser_group = pygame.sprite.Group()
        self.meteor_group = pygame.sprite.Group()
        self.background_surface = pygame.image.load("data/graphics/background.png")
        self.score_ui = Score()

        self.laser_shoot_sound = pygame.mixer.Sound("data/sounds/laser.ogg")
        self.explosion_sound = pygame.mixer.Sound("data/sounds/explosion.wav")
        self.background_music = pygame.mixer.Sound("data/sounds/music.wav")
        self.background_music.play(loops=-1)

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == EventSystem().user_event_slot:
                    if event.custom_event_type == GameEvents.PLAYER_PRIMARY_SHOOT:
                        self.laser_shoot_sound.play()
                        Laser(
                            position=self.ship.rect.midtop,
                            groups=self.laser_group,
                        )
                    if event.custom_event_type == GameEvents.METEOR_TIMER_COMPLETE:
                        Meteor(groups=self.meteor_group)
                    if event.custom_event_type == GameEvents.SHIP_DESTROYED:
                        pygame.quit()
                        sys.exit()
                    if event.custom_event_type == GameEvents.METEOR_DESTROYED:
                        self.explosion_sound.play()

            dt: float = self.clock.tick(FPS) / 1000.0

            self.spaceship_group.update(delta_time=dt, meteor_group=self.meteor_group)
            self.laser_group.update(delta_time=dt, meteor_group=self.meteor_group)
            self.meteor_group.update(delta_time=dt)

            self.display_surface.fill("black")
            self.display_surface.blit(self.background_surface, (0, 0))

            self.score_ui.display()

            display_fps(self.clock, WINDOW_WIDTH)

            self.spaceship_group.draw(self.display_surface)
            self.laser_group.draw(self.display_surface)
            self.meteor_group.draw(self.display_surface)

            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
