from pico2d import *

open_canvas(800, 450)

player = load_image('rockman_run.png')
bg = load_image('kirby_castle.png')

def rockman_run(frame_x, frame_y, width, height, x, y):
    clear_canvas()
    bg.draw_now(400, 225)
    player.clip_draw(frame_x, frame_y, width, height, x, y)
    update_canvas()

time = 0.1

select = 'rockman'

if select == 'rockman':
    x = 40
    frame_x = 0
    frame_y = 3

    while x < 760:
        rockman_run(frame_x * 160, frame_y * 170, 180, 180, x, 70)
        frame_x = (frame_x + 1) % 5

        if frame_x == 0:
            x += 60
            if frame_y == 3:
                frame_y = 2
            elif frame_y == 2:
                frame_y = 3

        x += 20
        delay(time)
        get_events()

    frame_x = 4
    frame_y = 0

    while x > 40:
        rockman_run(frame_x * 160, frame_y * 170, 180, 180, x, 90)
        frame_x -= 1

        if frame_x < 0:
            frame_x = 4
            x -= 60

        if frame_x == 0:
            frame_y = (frame_y + 1) % 2

        x -= 20
        delay(time)
        get_events()