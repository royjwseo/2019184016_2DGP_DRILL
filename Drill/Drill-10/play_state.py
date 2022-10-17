from pico2d import *
import game_framework
import title_state
import logo_state
import item_state
import add_state
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir=1

        self.image = load_image('animation_sheet.png')
        self.item=None
        self.ball_image=load_image('ball21x21.png')
        self.big_ball_image=load_image('ball41x41.png')
    def update(self):
        self.frame = (self.frame + 1) % 8

        self.x += self.dir*1
        if self.x>800:
            self.x=800
            self.dir=-1
        elif self.x<0:
            self.x=0
            self.dir=1


    def draw(self):
        if self.dir==1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        elif self.dir ==-1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        if self.item=='Ball':
            self.ball_image.draw(self.x+10,self.y+50)
        elif self.item=='BigBall':
            self.big_ball_image.draw(self.x+10,self.y+50)
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key==SDLK_i:
                game_framework.push_state(item_state)
            elif event.key==SDLK_b:
                game_framework.push_state(add_state)

boy=None #NULL
boy1=None
boy2=None
boy3=None
boy4=None
boy5=None
boy6=None
boy7=None
boy8=None

i=0

grass=None
team=[boy1,boy2,boy3,boy4,boy5,boy6,boy7,boy8]
#running=True

#초기화 ->객체들을 생성하는 함수를 구조화
def enter():
    global boy,grass,running,team,i

    team[i]=Boy()
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

    #team.update()

def draw(): #월드를 그리는 함수
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world(): #item state에서 배경 만들어주기위해 없애지 않는 그리기 함수 생성
    grass.draw()
    boy.draw()
   # team.draw()

def pause():
    pass

def resume():
    pass
#main.py로 옮김 구조화하여
#open_canvas()

#enter()
# game main loop code
#while running:
 #   handle_events()

    ##boy.update() ->update로 변경
  #  update()

    ##clear_canvas()
    ##grass.draw()
    ##boy.draw()
    ##update_canvas() -> draw
   # draw()
#    delay(0.05)

#exit()
# finalization code
#close_canvas()
