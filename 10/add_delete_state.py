import pico2d
from pico2d import *

import game_framework
import play_state

image = True


def enter():
    global image
    image = load_image('add_delete_boy.png')
    pass


def exit():
    global image
    del image
    pass


def update():
    pass


def draw():
    global image
    clear_canvas()
    play_state.draw_world()
    image.draw(400, 300)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_q:
                    game_framework.pop_state()
                case pico2d.SDLK_KP_PLUS:
                    play_state.boy.append(play_state.Boy())
                    game_framework.pop_state()
                case pico2d.SDLK_KP_MINUS:
                    if len(play_state.boy) - 1 > 0:
                        del(play_state.boy[len(play_state.boy) - 1])
                    game_framework.pop_state()
