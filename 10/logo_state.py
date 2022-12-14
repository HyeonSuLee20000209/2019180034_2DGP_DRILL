from pico2d import *

import game_framework
import title_state

running = True
image = True
logo_time = True


def enter():
    global image
    image = load_image('tuk_credit.png')
    pass


def exit():
    global image
    del image
    pass


def update():
    global logo_time
    # global running
    if logo_time > 2.0:
        logo_time = 0
        game_framework.change_state(title_state)
    delay(0.01)
    logo_time += 0.01


def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def handle_events():
    events = get_events()
