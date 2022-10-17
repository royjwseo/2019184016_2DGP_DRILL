import pico2d
import play_state
import logo_state

start_state=logo_state #모듈을 변수로 취급
pico2d.open_canvas()
states=[logo_state,play_state]

# game main loop code
for state in states:
    state.enter()
    while state.running:
        state.handle_events()
        # boy.update() ->update로 변경
        state.update()

        # clear_canvas()
        # grass.draw()
        # boy.draw()
        # update_canvas() -> draw
        state.draw()
        if state==logo_state:
            pico2d.delay(0.5)
        else:
            pico2d.delay(0.01)

    state.exit()
# finalization code
pico2d.close_canvas()
