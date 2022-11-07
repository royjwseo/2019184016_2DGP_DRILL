from pico2d import *
import game_framework
import game_world
from boy import Boy
from grass import Grass #grass 라는 모듈로부터 Grass라는 클래스 받아옴
from grass1 import Grass1
boy=None




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
    global boy
    boy = Boy()
    grass = Grass()
    grass1=Grass1()
    game_world.add_object(boy,1)
    game_world.add_object(grass,0)
    game_world.add_object(grass1,1)


# 종료
def exit():
    game_world.clear()
    pass

def update():


    for game_object in game_world.all_objects():
        game_object.update()

def draw_world():

    for game_object in game_world.all_objects():
        game_object.draw()
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
