import pygame
from flappy.helpers import get_image_path
from constants import PIPE_WIDTH, PIPE_HEIGHT, GAME_SPEED, SCREEN_HEIGHT


class Pipe(pygame.sprite.Sprite):
    def __init__(self, y_pos, width, offset, inverted):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(
            pygame.image.load(get_image_path("pipe-red.png")).convert_alpha(),
            (PIPE_WIDTH, PIPE_HEIGHT),
        )

        self.inverted = inverted
        self.scored = False
        self.rect = self.image.get_rect()
        self.rect[0] = width

        if self.inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = SCREEN_HEIGHT - y_pos - offset - PIPE_HEIGHT
        else:
            self.rect[1] = SCREEN_HEIGHT - y_pos

    def update(self):
        self.rect[0] -= GAME_SPEED
