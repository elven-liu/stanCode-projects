"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program is to make the animation logic for the breakoutgraphics.py to properly work. Users click and the ball and
the paddle start moving, and users have 3 lives to break all the bricks.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    graphics.write_live(lives)
    while True:
        # This is to calculate the lives, change the switcher and display the lives in the window.
        if graphics.ball_drops():
            graphics.click_button = True
            lives -= 1
            graphics.remove_live()
            if lives > 0:
                graphics.reset_ball()
                graphics.write_live(lives)
            else:
                graphics.write_death()
                break
        graphics.start_game()
        # If the switch is off, the ball, paddle will start moving.
        if not graphics.click_button:
            graphics.move_ball()
            graphics.collision()
        pause(FRAME_RATE)



if __name__ == '__main__':
    main()
