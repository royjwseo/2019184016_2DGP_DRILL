from pico2d import *
import game_framework
from boy import Boy
from grass import Grass #grass 라는 모듈로부터 Grass라는 클래스 받아옴

boy = None
grass = None





def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if (event.type, event.key) == (SDL_KEYDOWN,SDLK_ESCAPE):
            game_framework.quit()
        else:
            boy.hand_event(event) #소년한테 이벤트를 처리하도록 요청,
# 초기화
def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()

# 종료
def exit():
    global boy, grass
    del boy
    del grass

def update():
    boy.update()

def draw_world():
    grass.draw()
    boy.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass




def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
