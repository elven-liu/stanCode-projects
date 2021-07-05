"""
File: hailstone.py
Name:
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    Users enter a number and this program will calculate how many steps can this number
    reach 1
    """
    print('This program computes Hailstone Sequence')
    number = int(input('Enter a number: '))
    step = 0

    """
    If number = 1, while loop will end and print out how many steps.
    If this number is odd, the number will re-define to a new number
    If this number is even, the number will also re-define to another new number.
    """
    while True:
        if number == 1:
            print('It took ' +str(step) +' steps to reach 1')
            break
        elif number % 2 == 1:
            new_num_odd = number*3 + 1
            step += 1
            print(str(number) +' is odd, so I make 3n+1: ' +str(new_num_odd))
            number = new_num_odd
        else:
            new_num_even = number // 2
            step += 1
            print(str(number) +' is even, so I take half: ' +str(new_num_even))
            number = new_num_even


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
