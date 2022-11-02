from pico2d import *

#2이벤트 정의
RD,LD,RU,LU,TIMER,A=range(6)

key_event_table={
    (SDL_KEYDOWN,SDLK_RIGHT): RD,
    (SDL_KEYDOWN,SDLK_LEFT):LD,
    (SDL_KEYUP,SDLK_RIGHT):RD,
    (SDL_KEYUP,SDLK_LEFT):LU,
    (SDL_KEYDOWN,SDLK_a):A
}


#1상태 정의
class IDLE:
    def enter(self,event):#상태에 들어갈 때 행하는 액션
        print('Enter IDLE')
        self.dir=0
        self.timer=1000
        pass
    def exit(self):#상태를 나올 떄 행하는 액션, ex>고개돌기
        print('exit idle')
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
    def exit(self):  # 상태를 나올 떄 행하는 액션, ex>고개돌기
        print('exit run')
        self.face_dir=self.dir
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


class SLEEP:
    def enter(self,event):#상태에 들어갈 때 행하는 액션
        print('Enter IDLE')

        pass
    def exit(self):#상태를 나올 떄 행하는 액션, ex>고개돌기
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


class AUTO_RUN:
    @staticmethod


    def enter(self,event):  # 상태에 들어갈 때 행하는 액션
        print('enter run')
        #방향을 결정해야하는데, 뭘 근거로? 어떤 키가 눌렸기때문에?
        #키 이벤트 정보가 필요.
        go = True
        if event ==A:
            while(self.dir<799):
                self.dir+=1
            # elif(self.dir>0 and go==False):
            #     self.dir-=1
            #     if(self.x<=0):
            #         go=True




        pass
    @staticmethod
    def exit(self):  # 상태를 나올 떄 행하는 액션, ex>고개돌기
        print('exit run')
        self.face_dir=self.dir
        pass
    @staticmethod
    def do(self):
        self.frame=(self.frame+1)%8
        #x좌표 변경, 달리기

        self.x += self.dir

        #self.x+=self.dir
        self.x=clamp(0,self.x,800)

        pass
    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_composite_draw(self.frame*100, 0, 100, 100, self.x, self.y,200,200)
        elif self.dir == 1:
            self.image.clip_composite_draw(self.frame*100, 100, 100, 100, self.x, self.y,200,200)
        pass

next_state={
    SLEEP:{RD:RUN,LD:RUN,RU:RUN,LU:RUN,TIMER:SLEEP},
    IDLE:{RU:RUN,LU:RUN,RD:RUN,LD:RUN,TIMER:SLEEP},

    RUN:{RU:IDLE,LU:IDLE,RD:IDLE,LD:IDLE},
AUTO_RUN:{A:AUTO_RUN,A:AUTO_RUN}
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

    def __init__(self):
        self.x, self.y = 0, 90
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
            self.cur_state.exit(self)
            self.cur_state=next_state[self.cur_state][event]#다음 상태를 구한다.
            self.cur_state.enter(self,event) #다음 상태의 entry action수행
            
        
        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        
        self.cur_state.draw(self)
        

        # else:
