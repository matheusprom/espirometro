import pygame

from flappy.helpers import get_sound_path


class GameSound:

    @staticmethod
    def play_coin_sound():
        sound_path = get_sound_path("coin.wav")
        sound = pygame.mixer.Sound(sound_path)
        sound.play()

    @staticmethod
    def run_background_music():
        sound_path = get_sound_path("background.wav")
        sound = pygame.mixer.Sound(sound_path)
        sound.play(-1)
