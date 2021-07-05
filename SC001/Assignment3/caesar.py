"""
File: caesar.py
Name: Elven Liu
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    """
    Users will enter a number to shift all ALPHABET. Then users will enter a ciphered string and the program
    will translate the ciphered string to the deciphered one.
    """

    number = int(input('Secret number: '))
    word = input("What's the ciphered string? ")
    word = word.upper()

    ans = ""
    for i in range(len(word)):
        # for sentences with blanks to print " "
        if word[i] == " ":
            ans += " "
        else:
            p = ALPHABET.find(word[i])
            # for the scenario that p can be found in the ALPHABET
            if p != -1:
                if p + number >= len(ALPHABET):
                    ans += ALPHABET[p + number - len(ALPHABET)]
                else:
                    ans += ALPHABET[p + number]
            # to print the punctuation marks(, . ! ?)
            else:
                ans += word[i]

    print('The deciphered string is: ' +str(ans))


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
