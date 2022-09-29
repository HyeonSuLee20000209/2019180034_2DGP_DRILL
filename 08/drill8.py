from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 800, 600

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dir_x, dir_y = 0, 0
right = 1
left = 0
dir = 0

def handle_events():
    global running
    global dir_x, dir_y
    global x, y
    global dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_q or event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_LEFT:
                dir = left
                dir_x -= 1
            elif event.key == SDLK_RIGHT:
                dir = right
                dir_x += 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_RIGHT:
                dir_x -= 1
    pass

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2, 800, 600)
    
    # 뒤 돌아 볼때 사용
    if dir_x > 0:
        dir = right
    elif dir_x < 0:
        dir = left

    character.clip_draw(frame * 100, 100 * dir, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    
    # 화면 밖으로 안 나가게 하기
    if 20 < x + dir_x * 5 < TUK_WIDTH - 20:
        x += dir_x * 5
    if 25 < y + dir_y * 5 < TUK_HEIGHT - 25:
        y += dir_y * 5

    delay(0.01)

close_canvas()
