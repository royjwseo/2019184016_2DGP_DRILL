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
    image=load_image('add_delete_boy.png')

    # fill here
    pass

def exit():
    global image
    del image #객체 날리는 키워드 del

    # fill here
    pass

def update():
    #logo time을 계산하고, 그결과에 따라 1초가 넘으면 running =false
    play_state.update()
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400,300)
    update_canvas()
    # fill here
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_j:
                    play_state.enter()
                    game_framework.pop_state()
                case pico2d.SDLK_j:
                    play_state.enter()
                    game_framework.pop_state()

            if event.key == SDLK_ESCAPE:
                game_framework.pop_state()#이전 상태인 play로 복귀





