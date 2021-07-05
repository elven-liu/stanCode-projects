"""
File: hangman.py
Name: Elven Liu
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    The program will randomly choose a English words for users to guess. At first, users will know how long is the word.
    Users will have N_TURNS to guess the word incorrectly.
    """
    word = random_word()
    new_word = new(word)
    print('You have ' + str(N_TURNS) + ' guesses left.')
    print('The word looks like:' + str(new_word))

    first_guess = input('Your guess:')
    first_guess = first_guess.upper()
    j = 0  # j represents the times that users guess incorrectly.
    new_word = ""
    # If users enter 2 or 2 more alphabet or not alphabet, the program will display illegal format.
    if first_guess.isalpha() is False or len(first_guess) > 1:
        print('illegal format.')
    else:
        """
        After first guess, if the alphabet is in the answer string, the program will display 
        which places is the alphabet.
        """
        for i in range(len(word)):
            if first_guess == word[i]:
                new_word += first_guess
            else:
                new_word += '-'
        if first_guess in word:
            print('You have ' + str(N_TURNS) + ' guesses left.')
            print('The word looks like:' + str(new_word))
        # If the alphabet is not in the answer, guess chance will be N_TURNS - 1
        else:
            j += 1
            print("There's no " + str(first_guess) + "'s in the word.")
            print('You have ' + str(N_TURNS - j) + ' guesses left.')
            print('The word looks like:' + str(new_word))

    # From the second guess, the program will run this function.
    while j <= N_TURNS:
        whole_new_word = ""
        later_guess = input('Your guess:')
        later_guess = later_guess.upper()
        # Illegal format
        if later_guess.isalpha() is False or len(later_guess) > 1:
            print('illegal format.')
            print('You have ' + str(N_TURNS - j) + ' guesses left.')
        # Legal format
        else:
            # The guess alphabet is in the answer.
            for k in range(len(word)):
                if later_guess == word[k]:
                    whole_new_word += later_guess
                else:
                    whole_new_word += '-'
            # The guess alphabet is not in the answer.
            if later_guess not in word:
                print("There's no " +str(later_guess) +"'s in the word." )
                j += 1

            # Store_word will store the first_guess word and later_guess words.
            store_word = ""
            for q in range(len(word)):
                if new_word[q].isalpha():
                    store_word += new_word[q]
                elif whole_new_word[q].isalpha():
                    store_word += whole_new_word[q]
                else:
                    store_word += '-'
            new_word = store_word
            if (N_TURNS - j) > 0 :
                if new_word == word:
                    print('You win!! The word was ' + str(word))
                    break
                else:
                    print('The word looks like:' + str(new_word))
                    print('You have ' + str(N_TURNS - j) + ' guesses left.')
            else:
                print('You are completely hung : ( The word was ' + str(word))
                break


def new(word):
    dash = ""
    for i in range(len(word)):
        dash += "-"
    return dash


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
