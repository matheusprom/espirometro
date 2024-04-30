import random
import pygame
from flappy.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    CLOCK_TICK,
    CAPTION,
    DISTANCE_BETWEEN_PIPES,
    MIN_PIPE_Y,
    MAX_PIPE_Y,
    MIN_PIPE_OFFSET,
    MAX_PIPE_OFFSET,
    SCORE_FONT_SIZE,
)
from flappy.helpers import get_image_path, get_sound_path, create_pygame_font
from flappy.models.ground import Ground
from flappy.models.pipe import Pipe
from flappy.models.bird import Bird


class Runner:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(CAPTION)

        self.clock = pygame.time.Clock()
        self.background = self.create_background()
        self.run_background_music()

        self.bird_group = pygame.sprite.Group()
        self.ground_group = pygame.sprite.Group()
        self.pipe_group = pygame.sprite.Group()

        self.score_font = create_pygame_font(SCORE_FONT_SIZE, bold=True)
        self.score = 0

        self.bird_group.add(Bird())

        for i in range(2):
            self.ground_group.add(Ground(i * SCREEN_WIDTH))

        for p in self.create_random_pipes(SCREEN_WIDTH):
            self.pipe_group.add(p)

        for p in self.create_random_pipes(SCREEN_WIDTH + DISTANCE_BETWEEN_PIPES):
            self.pipe_group.add(p)

    def run_background_music(self):
        sound_path = get_sound_path("background.wav")
        sound = pygame.mixer.Sound(sound_path)
        sound.play(-1)

    def create_score_text(self, score):
        return self.score_font.render(score, True, (255, 255, 255))

    @staticmethod
    def create_background():
        bg = pygame.image.load(get_image_path("background-day.png"))
        return pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def has_collision(self):
        for group in [self.ground_group, self.pipe_group]:
            if pygame.sprite.groupcollide(
                self.bird_group, group, False, False, pygame.sprite.collide_mask
            ):
                return True

        return False

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                for bird in self.bird_group.sprites():
                    bird.bump()

    def update_ground(self):
        current_ground = self.ground_group.sprites()[0]
        if current_ground.rect[0] <= -current_ground.rect[2]:
            current_ground.kill()
            self.ground_group.add(Ground(SCREEN_WIDTH))

    def update_pipe(self):
        p1 = self.pipe_group.sprites()[0]
        if p1.rect[0] <= -p1.rect[2]:
            self.pipe_group.sprites()[0].kill()
            self.pipe_group.sprites()[0].kill()

            for p in self.create_random_pipes(SCREEN_WIDTH):
                self.pipe_group.add(p)

    def create_random_pipes(self, width):
        y_pos = random.randint(MIN_PIPE_Y, MAX_PIPE_Y)
        offset = random.randint(MIN_PIPE_OFFSET, MAX_PIPE_OFFSET)

        p1 = Pipe(y_pos, width, offset, True)
        p2 = Pipe(y_pos, width, offset, False)

        return p1, p2

    def play_coin_sound(self):
        sound_path = get_sound_path("coin.wav")
        sound = pygame.mixer.Sound(sound_path)
        sound.play()

    def update_score(self):
        for bird in self.bird_group:
            for pipe in self.pipe_group:
                bird_center = (bird.rect[0] + bird.rect[2]) / 2
                pipe_center = (pipe.rect[0] + pipe.rect[2]) / 2
                if not pipe.scored and pipe.inverted and bird_center >= pipe_center:
                    pipe.scored = True
                    self.score += 1
                    self.play_coin_sound()

    def update_frame(self):
        self.screen.blit(self.background, (0, 0))
        self.update_ground()
        self.update_pipe()

        for group in [self.pipe_group, self.ground_group, self.bird_group]:
            group.update()
            group.draw(self.screen)

        self.update_score()

        self.screen.blit(
            self.create_score_text(str(self.score)),
            ((SCREEN_WIDTH - (SCORE_FONT_SIZE / 2)) / 2, SCREEN_HEIGHT / 8),
        )
        pygame.display.update()

    def run(self):
        while not self.has_collision():
            self.clock.tick(CLOCK_TICK)
            self.check_events()
            self.update_frame()

        pygame.quit()
