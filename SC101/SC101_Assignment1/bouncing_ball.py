"""
File: Bouncing ball
Name: Elven
-------------------------
This program is to simulate how balls bounce in the world. Users can click anywhere in the window and the ball will start
bouncing. Users can only click 3 times.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
number = 1
ball = GOval(SIZE, SIZE)
click_button = True


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(click)
    ball.filled = True
    ball.fill_color = 'magenta'
    ball.color = 'magenta'
    window.add(ball, START_X, START_Y)


def click(m):
    global number, ball, click_button
    speed = GRAVITY
    while click_button is True and number <= 3:
        # click button is to make sure when ball is bouncing, clicks do not mean anything.
        click_button = False
        # when ball drops from high place to lower place.
        while ball.x + SIZE <= 800:
            while ball.y + SIZE <= 500:
                ball.move(VX, speed)
                speed += GRAVITY
                pause(DELAY)
            speed = speed * REDUCE
            # when ball bounce back from low place to higher one and ball will change the direction when the speed = 0
            while speed >= 0:
                ball.move(VX, speed * -1)
                speed -= GRAVITY
                pause(DELAY)
        # when ball is getting out of the window, it will get back to the original place.
        ball.x = START_X
        ball.y = START_Y
    # when the ball gets back to the original place, the click button will turn on again.
    if ball.x == START_X and ball.y == START_Y:
        click_button = True
        number += 1





if __name__ == "__main__":
    main()
