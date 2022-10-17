from pico2d import *
import game_framework
import play_state
import title_state
# fill here
# running=True framework 추가시 필요 x
image=None
logo_time=0.0



def enter():
    global image
    image=load_image('tuk_credit.png')

    # fill here
    pass

def exit():
    global image
    del image #객체 날리는 키워드 del

    # fill here
    pass

def update():
    #logo time을 계산하고, 그결과에 따라 1초가 넘으면 running =false
    global logo_time,running
    delay(0.01)
    logo_time+=0.01
    if logo_time>=0.5:
        logo_time=0
        # running=False gameframework추가시 quit이용 다른 state이동시 changestate
        game_framework.change_state(title_state)
    # fill here
    pass

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    # fill here
    pass

def handle_events():
    events = get_events()





