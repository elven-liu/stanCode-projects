"""
File: Draw lines
Name: Elven Liu
-----------------------

Users can click anywhere in the window first and that place will have a ball. And users click another place in the window,
then this place and the circle will connect to be a line.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10

window = GWindow()
number = 0
m_x = 0
m_y = 0
circle = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(line)


def line(m):
    global number, m_x, m_y, circle
    # when number = 0, if you click, that place will have a ball.
    if number == 0:
        circle = GOval(SIZE, SIZE)
        circle.color = 'black'
        window.add(circle, m.x - SIZE/2, m.y - SIZE/2)
        m_x = m.x - SIZE/2
        m_y = m.y - SIZE/2
        number += 1
    # when number = 1, if you click, that place will connect with the ball to be a line.
    else:
        straight = GLine(m_x, m_y, m.x, m.y)
        straight.color = 'black'
        window.add(straight)
        window.remove(circle)
        # when the line appears, the number will be 0 and start from drawing the ball.
        number -= 1


if __name__ == "__main__":
    main()
