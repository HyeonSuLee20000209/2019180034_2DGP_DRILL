import pico2d
from pico2d import *
import game_framework
import title_state
import item_state
import add_delete_state


left = -1
right = 1


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir = right
        self.image = load_image('animation_sheet.png')
        self.item = None
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        if self.x > 800:
            self.x = 800
            self.dir = left
        elif self.x < 0:
            self.x = 0
            self.dir = right

    def draw(self):
        if self.dir == left:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == right:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)

        if self.item == 'Ball':
            self.ball_image.draw(self.x + 10 * self.dir, self.y + 50)
        elif self.item == 'BigBall':
            self.big_ball_image.draw(self.x + 10 * self.dir, self.y + 50)


def handle_events():
    global running
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
                case pico2d.SDLK_i:
                    game_framework.push_state(item_state)
                case pico2d.SDLK_b:
                    game_framework.push_state(add_delete_state)


boy = []
grass = None
running = True

def enter():
    global boy, grass, running
    boy.append(Boy())
    grass = Grass()
    running = True


# finalization code
def exit():
    global boy, grass
    del boy
    del grass


def update():
    global boy
    for clone in boy:
        clone.update()


def draw():
    global grass, boy
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    grass.draw()
    for clone in boy:
        clone.draw()


def pause():
    pass


def resume():
    pass
