"""
File: similarity.py
Name: Elven Liu
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    Users will input a long DNA stand and a short one. The program will help
    to find which part of the long strand are the most similar to the short one.
    """
    long_sequence = input('Please give me a DNA sequence to research: ')
    long_sequence = long_sequence.upper()
    short_sequence = input('What DNA sequence would you like to match? ')
    short_sequence= short_sequence.upper()

    # The first strand will be the standard to compare with other strands.
    score_1 = 0
    for i in range(len(short_sequence)):
        if short_sequence[i] == long_sequence[i]:
            score_1 += 1

    if score_1 == len(short_sequence):
        print('The best match')
    else:
        maximum = score_1
        j = 1   # j represents how many times should this program runs
        k = 0   # k represents the k-th alphabet in the short strand to compare with the q-th alphabet in the long one.
        maximum_string = ""
        while j <= len(long_sequence) - len(short_sequence):
            score_2 = 0
            q = len(short_sequence)
            for q in range(j, j+len(short_sequence)):
                if short_sequence[k] == long_sequence[q]:
                    score_2 += 1
                k += 1
            k = 0
            j += 1
            # This function is to find the max string.
            if score_2 > maximum:
                maximum = score_2
                maximum_string = long_sequence[j-1: j + len(short_sequence)-1]
            else:
                score_2 = 0

    print('The best match is: ' +str(maximum_string) )



###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
