from pico2d import *

import sys
height=0
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
def handle_events():
    # fill here
    global running
    global dir
    global hir
    global height
    global countx
    global county
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                height=1

                dir += 1
            elif event.key == SDLK_LEFT:
                height=0

                dir -= 1
            elif event.key == SDLK_UP:
                if(height==0):
                    height=2
                elif(height==1):
                    height =3

                hir += 1
            elif event.key == SDLK_DOWN:
                if (height == 0):
                    height = 2
                elif (height == 1):
                    height = 3

                hir -= 1
            elif event.key == SDLK_ESCAPE:

                running == False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:

                dir -= 1
            elif event.key == SDLK_LEFT:

                dir += 1
            if event.key == SDLK_UP:

                hir -= 1
            elif event.key == SDLK_DOWN:

                hir += 1


open_canvas(TUK_WIDTH,TUK_HEIGHT)
grass = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
running=True
handle_events()
x = 400
frame = 0
dir = 0
y=300
hir=0


while running:


    clear_canvas()
    grass.draw(640, 512)

    character.clip_draw(frame * 100, 100 * height, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    if x < 0:
        sys.exit()
    elif x > TUK_WIDTH:
        sys.exit()
    if y < 0:
        sys.exit()
    elif y > TUK_HEIGHT:
        sys.exit()

    x += dir * 5

    y+=hir*5

    delay(0.01)

close_canvas()
