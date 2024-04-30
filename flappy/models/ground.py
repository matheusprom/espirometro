import pygame
from flappy.helpers import get_image_path
from flappy.constants import SCREEN_HEIGHT, GAME_SPEED, SCREEN_WIDTH, GROUND_HEIGHT


class Ground(pygame.sprite.Sprite):
    def __init__(self, x_pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(
            pygame.image.load(get_image_path("base.png")).convert_alpha(),
            (SCREEN_WIDTH, GROUND_HEIGHT),
        )

        self.rect = self.image.get_rect()
        self.rect[0] = x_pos
        self.rect[1] = SCREEN_HEIGHT - GROUND_HEIGHT

    def update(self):
        self.rect[0] -= GAME_SPEED
