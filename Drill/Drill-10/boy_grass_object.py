from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 1

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

boy=None #NULL
grass=None
running=True

#초기화 ->객체들을 생성하는 함수를 구조화
def enter():
    global boy,grass,running

    boy = Boy()
    grass = Grass()
    running = True

#종료 함수
def exit():
    global boy,grass
    del boy
    del grass

#월드에 존재하는 객체들을 업데이트한다.
#이 게임에서 grass는 움직이지 않으므로 굳이 업데이트를 반복할 필요 x->생략
def update():
    boy.update()


def draw(): #월드를 그리는 함수
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

open_canvas()

enter()
# game main loop code
while running:
    handle_events()

    #boy.update() ->update로 변경
    update()

    #clear_canvas()
    #grass.draw()
    #boy.draw()
    #update_canvas() -> draw
    draw()
    delay(0.05)

exit()
# finalization code
close_canvas()
