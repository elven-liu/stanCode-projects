from karel.stanfordkarel import *

"""
File: MidpointKarel.py
Name: Elven Liu
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    Karel will put beepers in the first street and come back to the original place. Karel will start picking up beepers
    from the left side and the right side. In the end, Karel will find the midpoint of the checkerboard.
    """
    if facing_east():
        if front_is_clear():
            put_beeper_in_1_street()
            check_midpoint()
        else:
            # for the 1x1 checkerboard.
            put_beeper()


def put_beeper_in_1_street():
    """
    Pre-Condition: Karel is at street 1 avenue 1, facing East.
    Post-Condition: Karel will put beepers in the first street and come back to street 1 avenue 1.
    """
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()
    turn_around()

    while front_is_clear():
        move()
    turn_around()


def check_midpoint():
    """
    Pre-Condition: Karel is at street 1 avenue 1, facing East.
    Post-Condition: Karel will pick up beepers from the leftmost side then the rightmost side. And he will gradually
    find the midpoint, facing South or North.
    """

    while on_beeper():
        pick_beeper()
        move()
        while on_beeper() and front_is_clear():
            move()
        turn_around()
        if not on_beeper():
            move()
    turn_left()
    put_beeper()


def turn_around():
    for i in range(2):
        turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
