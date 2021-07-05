from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
Name: Elven Liu
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""


def main():
    """
    Karel will help to put beepers to build the pillar
    """
    while front_is_clear():
        build_pillar()
        down()
    build_pillar()
    end()


def build_pillar():
    """
    Pre-condition: Karel is at the bottom of the pillar, facing East.
    Post-condition: Karel is finishing building the pillar and
    is at the top of the pillar, facing North.
    """
    turn_left()
    while front_is_clear():
        if not on_beeper():
            put_beeper()
            move()
        else:
            move()
    if not on_beeper():
        put_beeper()


def down():
    """
    Pre-condition: Karel is at the top of the pillar, facing North.
    Post-condition: Karel is at the bottom of the next pillar, facing East.
    """
    turn_right()
    for i in range(4):
        move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


def end():
    """
    Pre-condition: Karel is at the top of the pillar, facing North.
    Post-condition: Karel goes down to the bottom of the pillar, facing East.
    """
    turn_around()
    while front_is_clear():
        move()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
