

table={
    'SLEEP':{"HIT":"WAKE"},
    "WAKE":{"TIMER10":"SLEEP"}
}

cur_state='SLEEP'
event='HIT'
next_state=table[cur_state][event]
print(table[cur_state]['HIT'])
print(table['WAKE']['TIMER10'])











# # class Star:#이때의 클래스의 역할: 함수 또는 변수를 묶는다 그룹이름으로.
# #     x=100
# #     def change():
# #         x=200
# #         print('x is ',x)
# #
# #
# # print(Star.x) #Star 클래스 x는 클래스 변수
# # Star.change() #클래스 함수 호출 ,,,변수나 함술를 묶어내어 그루핑하는 역할을 클래스가 함
# #
# #
# # star=Star() #비록 객체생성용이 아니어도 객체는 만들어진다.
# # star.change()
#
# class Player:
#     def __init__(self):
#         self.x=100
#     def where(self):
#         print(self.x)
#
# player=Player()
# player.where()#객체 함수 호출-- Player.where(player) player라는 객체의 클래스의 함수를 호출하며 자신인 객체를 인자로 넘겨줌
#
# #Player.where() #클래스의 함수를 호출
# Player.where(player)