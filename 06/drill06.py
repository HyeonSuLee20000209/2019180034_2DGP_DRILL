from pico2d import*
from math import *

open_canvas()

grass = load_image('grass.png')

player = load_image('character.png')

x = 400

y = 90

direction = 0

count = 0

theta = 0

while 1:
    if count % 2 == 0:
        if direction == 0:
            while x < 800:
                clear_canvas_now()
                grass.draw_now(400,30)
                player.draw_now(x, y)
                x += 2

                if x == 800:
                    direction = 1
                    break
                if x == 400:
                    count += 1
                    break
                
        elif direction == 1:
            while y < 600:
                clear_canvas_now()
                grass.draw_now(400,30)
                player.draw_now(x, y)
                y += 2

                if y == 600:
                    direction = 2
                    break
                
        elif direction == 2:
            while x > 0:
                clear_canvas_now()
                grass.draw_now(400,30)
                player.draw_now(x, y)
                x -= 2

                if x == 0:
                    direction = 3
                    break
                
        elif direction == 3:
            while y > 90:
                clear_canvas_now()
                grass.draw_now(400,30)
                player.draw_now(x, y)
                y -= 2

                if y == 90:
                    direction = 0
                    break
    elif count % 2 == 1:        
        
        clear_canvas_now()
        grass.draw_now(400,30)
        player.draw_now(400 + 300 * cos(radians(theta)), 300 + 200 * sin(radians(theta)))
        theta += 1
        if theta == 360:
            count += 1
            theta = 0
close_canvas()
