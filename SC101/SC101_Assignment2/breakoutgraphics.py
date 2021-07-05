"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

This program is to draw the breakout game scene and make functions for the main function to create animations.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 3  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.
FRAME_RATE = 10

number = 1
click_button = True


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window_width = window_width
        self.window_height = window_height
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.paddle = GRect(self.paddle_width, self.paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = '#46373B'
        self.paddle.color = '#46373B'
        self.window.add(self.paddle, (self.window_width - self.paddle_width)/2, self.window_height - self.paddle_height - paddle_offset)

        # Center a filled ball in the graphical window
        self.ball_radius = ball_radius
        self.ball = GOval(self.ball_radius * 2, self.ball_radius * 2)
        self.ball.filled = True
        self.ball.fill_color = '#5995DD'
        self.ball.color = '#5995DD'
        self.window.add(self.ball, (self.window_width - ball_radius)/2, (self.window_height - ball_radius)/2)

        # Draw bricks
        brick_y = 0
        for i in range(brick_cols):
            brick_x = 0
            for j in range(brick_rows):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if (i + 1) / 2 <= 1:
                    self.brick.fill_color = '#1FBCD3'
                    self.brick.color = '#1FBCD3'
                elif 2 >= (i + 1) / 2 > 1:
                    self.brick.fill_color = '#CBE2B4'
                    self.brick.color = '#CBE2B4'
                elif 3 >= (i + 1) / 2 > 2:
                    self.brick.fill_color = '#F7BFA8'
                    self.brick.color = '#F7BFA8'
                elif 4 >= (i + 1) / 2 > 3:
                    self.brick.fill_color = '#F6B6CA'
                    self.brick.color = '#F6B6CA'
                else:
                    self.brick.fill_color = '#9BD5BD'
                    self.brick.color = '#9BD5BD'
                self.window.add(self.brick, brick_x, brick_y + brick_offset)
                brick_x += brick_width + brick_spacing
            brick_y += brick_height + brick_spacing

        # Default initial velocity for the ball
        self.__dx = random.randint(0, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

        """
        This switcher is to make sure that after user click the mouse, any other clicks does not mean anything until
        the ball drops
        """
        self.click_button = True

    # To display the lives in the window
    def write_live(self, lives):
        self.num = GLabel(f"☻LIVES: {lives}", x=self.window_width - 150, y=self.window_height)
        self.num.font = '-30'
        self.num.color = '#01514C'
        self.window.add(self.num)

    # To move lives in the window
    def remove_live(self):
        self.window.remove(self.num)

    # To display the death sentence when users use all lives
    def write_death(self):
        self.death = GLabel('You are DEAD!!!', x=20, y=self.window_height / 2)
        self.death.font = '-60'
        self.death.color = '#9C4803'
        self.window.add(self.death)

    # Once users click the mouse, the game will start.
    def start_game(self):
        onmouseclicked(self.click)

    # After users click, the paddle can move and the switcher transfers to 'False'
    def click(self, gaming):
        if 0 < gaming.x < self.window_width:
            onmousemoved(self.mouse_move)
            self.click_button = False

    # The ball will move depend on the initial velocity.
    def move_ball(self):
        self.ball.move(self.__dx, self.__dy)

    # The paddle can only move from the left wall to the right wall, and the paddle's y will be fixed.
    def mouse_move(self, event):
        if event.x < self.paddle_width/2:
            self.paddle.x = 0
        elif event.x > self.window_width - self.paddle_width/2:
            self.paddle.x = self.window_width - self.paddle_width
        else:
            self.paddle.x = event.x - self.paddle_width/2

    # Define the 'ball drop rule' that the ball drops out of the bottom margin.
    def ball_drops(self):
        ball_drops = self.ball.y > self.window_height
        return ball_drops

    # After ball drops out of the margin, the ball will come back to the original place.
    def reset_ball(self):
        self.window.add(self.ball, (self.window_width - self.ball_radius)/2, (self.window_height - self.ball_radius)/2)

    # Define the rule when the ball collide with the wall, brick and the paddle

    def collision(self):

        # When the ball bumps into the right, top and the left margin, the ball will bounce back.
        if self.ball.x <= 0 or self.ball.x >= self.window_width - self.ball_radius*2:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy

        # Define the 4 different angles that the ball collide with the object.
        obj_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        obj_2 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball_radius * 2)
        obj_3 = self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y)
        obj_4 = self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y + self.ball_radius * 2)

        # If the object is paddle, the ball will bounce back
        if obj_1 is not None or obj_2 is not None or obj_3 is not None or obj_4 is not None:
            if obj_1 == self.paddle or obj_2 == self.paddle or obj_3 == self.paddle or obj_4 == self.paddle:
                # This rule is to make sure that ball will not get into the paddle and keep changing the directions.
                if self.ball.x <= self.paddle.x or self.ball.x + self.ball_radius*2 >= self.paddle.x:
                    self.__dy = -self.__dy
                    self.ball.move(random.randint(0, MAX_X_SPEED), self.__dy - self.paddle_height)
                if self.ball.x <= self.paddle.x + self.paddle_width or self.ball.x + self.ball_radius*2 >= self.paddle.x + self.paddle_width:
                    self.__dy = -self.__dy
                    self.ball.move(random.randint(0, MAX_X_SPEED), self.__dy - self.paddle_height)
                self.__dy = -self.__dy
            # When the ball collides with bricks, the brick will remove.
            elif obj_1 != self.num and obj_2 != self.num and obj_3 != self.num and obj_4 != self.num:
                self.window.remove(obj_1)
                self.window.remove(obj_2)
                self.window.remove(obj_3)
                self.window.remove(obj_4)
                self.__dy = -self.__dy









