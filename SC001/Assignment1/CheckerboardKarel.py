from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
Name: Elven Liu
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""


def main():
    """
    Karel will put one beeper once every 2 checks to make it look like a checkerboard.
    """
    while facing_east():
        if front_is_clear():
            if facing_east():
                first_line()
            if left_is_clear():
                first_cross()
            if facing_west():
                second_line()
            if right_is_clear():
                second_cross()
        else:
            # for only 1 avenue and 1 check
            turn_left()
            first_line()


def first_line():
    """
    Pre-Condition: Karel is at the left of odd street(1,3,5,7...), facing East.
    Post-Condition: Karel is at the right of odd street,facing North.
    """
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()
    turn_left()


def first_cross():
    """
    Pre-Condition: Karel is at the right of odd street, facing North.
    Post-Condition: If front is clear, Karel will move to next street and at the right side, facing West.
    """
    if front_is_clear():
        if on_beeper():
            move()
            turn_left()
        else:
            move()
            turn_left()
            put_beeper()


def second_line():
    """
    Pre-Condition: Karel is at the right of even street(2,4,6,8...), facing West.
    Post-Condition: Karel is at the left of even street, facing North.
    """
    while front_is_clear():
        if on_beeper():
            on_beeper_move()
        else:
            not_on_beeper_move()
    turn_right()


def second_cross():
    """
        Pre-Condition: Karel is at the left of even street, facing North.
        Post-Condition: If front is clear, Karel will move to next street and at the left side, facing East.
    """
    if front_is_clear():
        move()
        turn_right()


def on_beeper_move():
    # Karel will move to next street based on the current location situation.
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()


def not_on_beeper_move():
    # Karel will move to next street based on the current location situation.
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear():
            move()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
