from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('girl.png')
x = 0
frame = 0
for x in range(0,800):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 60, 60, 60, 60, x, 90)
    update_canvas()
    frame = (frame + 1) % 8
    x += 5
    delay(0.001)
    get_events()

x=x-30;
for y in range(90,600):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 60, 0, 60, 60, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    y += 5
    delay(0.001)
    get_events()

for x in range(0,800):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 60, 120, 60, 60, 800-x, 560)
    update_canvas()
    frame = (frame + 1) % 8
    x += 5
    delay(0.001)
    get_events()
x=30
for y in range(90,600):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 60, 180, 60, 60, x, 690-y)
    update_canvas()
    frame = (frame + 1) % 8
    y += 5
    delay(0.001)
    get_events()

close_canvas()
