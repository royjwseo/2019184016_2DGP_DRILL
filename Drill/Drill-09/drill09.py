from pico2d import *
import random


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False



TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
hand_arrow = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')
tuk_ground = load_image('TUK_GROUND.png')
running = True
frame = 0
sheetline = 0
sx = TUK_WIDTH//2
sy = TUK_HEIGHT//2
x,y=sx,sy
ax,ay=x,y
t=0
ax = random.randint(0,TUK_WIDTH)
ay = random.randint(0, TUK_HEIGHT)
hand_arrow.draw(ax, ay)
def reset_world():
    global ax, ay
    global t
    global sx,sy
    global sheetline
    ax,ay=random.randint(0,TUK_WIDTH),random.randint(0,TUK_HEIGHT)
    t=0
    sx,sy=x,y
    if(ax>x):
        sheetline=1
    else:
        sheetline=0
    pass

def update_world():
    global x,y,t

    t+=0.001
    x=(1-t)*sx+t*ax
    y=(1-t)*sy+t*ay
    if t>=1.0:
        reset_world()

reset_world()
while running:
    update_world()
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand_arrow.draw(ax, ay)
    character.clip_draw(frame * 100, 100 * sheetline, 100, 100, x, y)
    update_canvas()

    frame = (frame + 1) % 8
    handle_events()




close_canvas()