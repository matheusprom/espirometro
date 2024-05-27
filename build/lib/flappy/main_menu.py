import pygame
import pygame_menu
from pygame_menu.examples import create_example_window
from flappy.helpers import get_image_path
from flappy.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    CAPTION,
)

from flappy.sound import GameSound

from typing import Optional

from flappy.runner import Runner

surface: Optional['pygame.Surface'] = None
main_menu: Optional['pygame_menu.Menu'] = None
background_image = pygame_menu.BaseImage(
    image_path= get_image_path('menu.jpg')
)


def main_background() -> None:
    background_image.draw(surface)


def run_background_music():
    background_music = GameSound()
    background_music.run_background_music()


def run_da_birdie():
    runner = Runner()
    runner.run()


def menuzao():
    global main_menu
    global surface

    surface = create_example_window(CAPTION, (SCREEN_WIDTH, SCREEN_HEIGHT))
    main_menu_theme = pygame_menu.themes.THEME_DARK
    main_menu_theme.set_background_color_opacity(0.5)  # 50% opacity

    main_menu = pygame_menu.Menu(
        height=SCREEN_HEIGHT * 0.4,
        onclose=pygame_menu.events.EXIT,  # User press ESC button
        theme=main_menu_theme,
        title='Blowy Bird',
        width=SCREEN_WIDTH * 0.6
    )

    main_menu.add.button('Play', run_da_birdie)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)


def game():
    global main_menu
    global surface

    pygame.init()

    pygame.display.set_caption(CAPTION)

    run_background_music()
    menuzao()

    running = True

    while running:

        main_background()
        if main_menu.is_enabled():
            main_menu.mainloop(surface, main_background)

    pygame.quit()
