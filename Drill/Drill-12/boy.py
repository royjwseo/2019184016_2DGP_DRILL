from pico2d import *
import play_state
import game_world
from ball import Ball

#2이벤트 정의
RD,LD,RU,LU,TIMER,SPACE=range(6)
event_name=['RD','LD','RU','LU','TIMER','SPACE']
key_event_table={
    (SDL_KEYDOWN,SDLK_SPACE): SPACE,
    (SDL_KEYDOWN,SDLK_RIGHT): RD,
    (SDL_KEYDOWN,SDLK_LEFT):LD,
    (SDL_KEYUP,SDLK_RIGHT):RD,
    (SDL_KEYUP,SDLK_LEFT):LU,

}


#1상태 정의
class IDLE:
    def enter(self,event):#상태에 들어갈 때 행하는 액션
        print('Enter IDLE')
        self.dir=0
        self.timer=1000
        pass
    def exit(self,event):#상태를 나올 떄 행하는 액션, ex>고개돌기
        print('exit idle')
        if event==SPACE:
            self.fire_ball()

        pass
    def do(self):
        self.frame=(self.frame+1)%8
        self.timer-=1
        if self.timer==0:
            self.add_event(TIMER)#좀 더 객체지향


        pass
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)


        pass



class RUN:
    @staticmethod
    def enter(self,event):  # 상태에 들어갈 때 행하는 액션
        print('enter run')
        #방향을 결정해야하는데, 뭘 근거로? 어떤 키가 눌렸기때문에?
        #키 이벤트 정보가 필요.
        if event ==RD:
            self.dir+=1
        elif event == LD:
            self.dir-=1
        elif event == RU:
            self.dir-=1
        elif event ==LU:
            self.dir +=1

        pass
    @staticmethod
    def exit(self,event):  # 상태를 나올 떄 행하는 액션, ex>고개돌기
        print('exit run')
        self.face_dir=self.dir
        if event==SPACE:
            self.fire_ball()


        pass
    @staticmethod
    def do(self):
        self.frame=(self.frame+1)%8
        #x좌표 변경, 달리기
        self.x+=self.dir
        self.x=clamp(0,self.x,800)

        pass
    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        pass

class Ball:
    image=None

    def __init__(self, x=800,y=300,velocity=1):
        if Ball.image==None:
            Ball.image=load_image('ball21x21.png')
        self.x,self.y,self.velocity=x,y,velocity

    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        self.x+=self.velocity

        if self.x<50 or self.x>750:
            game_world.remove_object(self)

class SLEEP:
    def enter(self,event):#상태에 들어갈 때 행하는 액션
        print('Enter IDLE')

        pass
    def exit(self,event):#상태를 나올 떄 행하는 액션, ex>고개돌기
        print('exit idle')
        pass
    def do(self):
        self.frame=(self.frame+1)%8
        pass
    def draw(self):
        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                           -3.141592/2,'',self.x+25, self.y-25,100,100)
        else:#오른쪽 눕기
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                           3.141592/2,'',self.x-25, self.y-25,100,100)


        pass

#3 상태 변환 기술



next_state={
    SLEEP:{RD:RUN,LD:RUN,RU:RUN,LU:RUN,SPACE:IDLE},
    IDLE:{RU:RUN,LU:RUN,RD:RUN,LD:RUN,TIMER:SLEEP,SPACE:IDLE},
    RUN:{RU:IDLE,LU:IDLE,RD:IDLE,LD:IDLE,SPACE:RUN},

}
class Boy:

    def add_event(self,event):
        self.q.insert(0,event)

    def hand_event(self,event):

        if(event.type,event.key)in key_event_table:
            key_event=key_event_table[(event.type,event.key)]
            self.add_event(key_event)

        # if event.type==SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             boy.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             boy.dir += 1
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             boy.dir += 1
        #             boy.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             boy.dir -= 1
        #             boy.face_dir = 1

    def fire_ball(self):
        print('FIRE BALL')
        ball=Ball(self.x,self.y,self.face_dir*2)
        game_world.add_object(ball,1)

    def __init__(self):
        self.x, self.y = 0, 50
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')
        
        self.q=[]#이벤트 큐 초기화
        self.cur_state=IDLE
        self.cur_state.enter(self,None) #초기 상태의 entry액션수행
        
    def update(self):
        
        self.cur_state.do(self)#현재 상태의do액션을 수행 그후 이벤트를 확인
        #이벤트를 확인해서 이벤트가 있음ㄴ 이벤트 변환 처리
        if self.q: #큐에 이벤트가 있으면, 이벤트가 발생했으면,
            event=self.q.pop()
            self.cur_state.exit(self,event)
            try:
                self.cur_state=next_state[self.cur_state][event]#다음 상태를 구한다.
            except KeyError:
                print(self.cur_state,event_name[event])
            self.cur_state.enter(self,event) #다음 상태의 entry action수행
            
        
        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        
        self.cur_state.draw(self)
        

        # else:
