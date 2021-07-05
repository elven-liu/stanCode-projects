"""
File: anagram.py
Name: Elven Liu
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

lst = []

def main():
    """
    TODO:
    """
    read_dictionary()
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        word = input('Find anagrams for: ')
        start = time.time()
        if word == EXIT:
            break
        else:
            print('Searching...')
            ans = find_anagrams(word)
            len_ans = len(ans)
            print(f'{len_ans} anagrams: {ans}')
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    global lst
    with open(FILE, 'r') as f:
        for line in f:
            lst.append(line.strip())


def find_anagrams(s):
    """
    :param s: str, word to look for the anagram
    :return: list, the full list of anagram
    """
    global lst
    ans_len = len(s)  # The length of the word
    search_lst = []  # Filtered list from the dictionary
    target = ''  # The answer found in the dictionary
    point = []  # The number location of the word.

    word = {}
    for j in range(ans_len):
        word[j] = s[j]

    # The dictionary will be filtered first to include the right length of words only.
    for i in range(len(lst)):
        if len(lst[i]) == ans_len:
            search_lst.append(lst[i])

    answer = find_anagrams_helper(word, [], search_lst, len(s), target, point)
    return answer


def find_anagrams_helper(word, ans_lst, sear_lst, ans_len, target, point):
    """

    :param word: dictionary, word to look for anagram
    :param ans_lst: list, anagrams will be put in this list
    :param sear_lst: list, filtered list from the read_dictionary
    :param ans_len: the length of the word
    :param target: str, the word that is found in the sear_lst
    :param point: the number location of the word.
    :return: list, the anagram list
    """

    if len(point) == ans_len:
        for i in range(ans_len):
            target += word[point[i]]
        if target not in ans_lst:
            if target in sear_lst:
                ans_lst.append(target)
                print(f'Found: {target}')
                print('Searching...')
        return ans_lst

    else:
        for i in range(ans_len):
            if i in point:
                pass
            else:
                point.append(i)
                find_anagrams_helper(word, ans_lst, sear_lst, ans_len, target, point)
                point.pop()
        return ans_lst


def has_prefix(sub_s):

    global lst
    for element in lst:
        if element.startwith(sub_s):
            break
        else:
            return False
    return True

if __name__ == '__main__':
    main()
