from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
Name: Elven Liu
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    """
    Karel is at Street 4 Avenue 3, facing East, and he has to find the door and pick up
    the newspaper (Street 3 Avenue 6) and come back to the original location, facing East.
    """
    find_newspaper()
    come_back()


def find_newspaper():
    """
    Pre-condition: Karel is at Street 4 Avenue 3, facing East
    Post-condition: Karel is at Street 3 Avenue 6, facing East, and he picks up the newspaper.
    """
    turn_right()
    move()
    turn_left()
    for i in range(3):
        move()
    pick_beeper()


def come_back():
    """
    Pre-condition: Karel is at Street 3 Avenue 6, facing East, and the newspaper is already in his hand.
    Post-condition: Karel is at Street 4 Avenue 3, facing East, and he puts the newspaper.
    """
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    for i in range(2):
        move()
    turn_around()
    put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
