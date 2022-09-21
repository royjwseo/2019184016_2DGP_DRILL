from pico2d import *

open_canvas()

# fill here

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
import math

x = 2
y = 90
r = 300
ang = 0
a = 400

count = -1
while (count % 2 == 0 or count == -1):

    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)

    if x == 398 and y == 90:
        count = count + 1
    if y == 90:
        x = x + 2
    if x == 798:
        y = y + 2
    if y == 598:
        x = x - 2
    if x == 2 and y != 90:
        y = y - 2

    delay(0.01)

close_canvas()

