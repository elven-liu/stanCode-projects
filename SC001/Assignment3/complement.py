"""
File: complement.py
Name: Elven Liu
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    Users can enter a DNA strand and the program will find the complement DNA stand.
    """
    dna = input('Please give me a DNA strand and I will find the complement: ')
    dna = dna.upper()
    new_dna = build_complement(dna)
    print('The complement of ' +str(dna) +' is ' +str(new_dna) )


def build_complement(dna):
    """
    :param dna: string, the DNA that users entered.
    :return: string, the complement DNA
    """
    ans = ""
    for base in dna:
        if base == 'A':
            ans += 'T'
        elif base == 'T':
            ans += 'A'
        elif base == 'C':
            ans += 'G'
        elif base == 'G':
            ans += 'C'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
