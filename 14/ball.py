import random
from pico2d import *
import game_world
import game_framework
import server


class Ball:
    image = None

    court = None

    def __init__(self):
        if Ball.court is None:
            Ball.court = load_image('futsal_court.png')

        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0 + 10, server.background.w - 10), random.randint(0 + 10, server.background.h - 10)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.sx, self.sy = self.x - server.background.window_left, self.y - server.background.window_bottom

        self.image.draw(self.sx, self.sy)

    def update(self):
        pass

    def handle_collision(self, other, group):
        if group == 'boy:ball':
            game_world.remove_object(self)
