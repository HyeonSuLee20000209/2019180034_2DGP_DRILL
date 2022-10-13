import pico2d
import play_state
import logo_state

states = [logo_state, play_state]

pico2d.open_canvas()

for state in states:
    state.enter()  # 초기화

    # 게임 루프
    while state.running:
        state.handle_events()
        state.update()
        state.draw()

    state.exit_program()

pico2d.close_canvas()
