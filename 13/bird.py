from pico2d import *
import game_framework


# Boy Run Speed
PIXEL_PER_METER = 10.0 / 0.1
RUN_SPEED_KMPH = 30.0
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000.0 / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


class Bird:
    def __init__(self, x, y):
        self.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.dir, self.face_dir = 1, 1
        self.frame_x, self.frame_y = 0, 2
        self.change_frame = False

    def update(self):
        self.frame_x = (self.frame_x + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0 + 25, self.x, 1400 - 25)

        if self.x + self.dir * RUN_SPEED_PPS * game_framework.frame_time > 1400 - 25:
            self.dir = -1
        elif self.x + self.dir * RUN_SPEED_PPS * game_framework.frame_time < 0 + 25:
            self.dir = 1

    def draw(self):
        if self.dir == -1:
            self.image.clip_composite_draw(int(self.frame_x) * 180, int(self.frame_y) * 169, 180, 169, 0, 'h', self.x, self.y, 50, 50)
        elif self.dir == 1:
            self.image.clip_draw(int(self.frame_x) * 180, int(self.frame_y) * 169, 180, 169, self.x, self.y, 50, 50)



