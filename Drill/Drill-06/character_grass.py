import math

from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
count = 0


def draw_c(x, y, t):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(t)


def run_circle():
    print('CIRCLE')

    cx = 400
    cy = 300
    r = 200
    for deg in range(270, 360, 5):
        x = cx + r * math.cos(deg / 360 * 2 * math.pi)
        y = cy + r * math.sin(deg / 180 * math.pi)
        draw_c(x, y, 0.1)
    for deg in range(0, 270, 5):
        x = cx + r * math.cos(deg / 360 * 2 * math.pi)
        y = cy + r * math.sin(deg / 180 * math.pi)
        draw_c(x, y, 0.1)


def run_rectangle():
    print('RECTANGLE')
    for x in range(400, 770 + 1, 10):
        draw_c(x, 90, 0.01)

    for y in range(90, 550 + 1, 10):
        draw_c(770, y, 0.01)

    for x in range(770, 10 + 1, -10):
        draw_c(x, 550, 0.01)

    for y in range(550, 90 + 1, -10):
        draw_c(50, y, 0.01)

    for x in range(10, 400 + 1, 10):
        draw_c(x, 90, 0.01)


while True:

    count += 1
    if count % 2 == 0:
        run_circle()
    else:
        run_rectangle()

close_canvas()
