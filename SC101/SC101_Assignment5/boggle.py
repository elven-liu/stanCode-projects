"""
File: boggle.py
Name: Elven Liu
----------------------------------------
This program is to find the words of boggle board which are in the dictionary.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

trigger = True
lst = []


def main():
    """
    Users enter the boggle letters. After entering, the program will start comparing the words with the dictionary list.
    """
    read_dictionary()
    all_letter = {}
    for i in range(4):
        word = input(f'{i + 1} row of letters: ')
        if len(word) == 7:
            if not word[1].isalpha() and not word[3].isalpha() and not word[5].isalpha():
                if word[0].isalpha() and word[2].isalpha() and word[4].isalpha() and word[6].isalpha():
                    word = word.lower()
                    for j in range(len(word)):
                        if word[j].isalpha():
                            col = i + 1
                            row = j // 2 + 1
                            all_letter[(col, row)] = word[j]
        else:
            print('illegal input')
            break
    start = time.time()
    search(all_letter)
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    global lst
    with open(FILE, 'r') as f:
        for line in f:
            if len(line.strip()) >= 4:
                lst.append(line.strip())


def search(board):
    """

    :param board: str, the letters user entered
    :return: lst, the letters found in the dictionary.
    """
    global lst
    final = []

    final_save = search_helper(board, 0, 0, [], [], [], '')

    for ele in final_save:
        final.append(ele)
    final_count = len(final)
    print(final)
    print('---------------')
    print(f'Found {final_count} words')


def search_helper(board, col, row, ans, current, location, target):
    """

    :param board: the letter user entered
    :param col: the column of the board
    :param row: the row of the board
    :param ans: lst, the answers that the program currently found in the dictionary.
    :param current: lst, the program run the recursive function and the program will store the letter in the current.
    :param location: the coordinate of letter
    :param target: str, after the length of current is more than 4, we will manipulate the string and look up the word in the dictionary.
    :return: the ans
    """
    global lst
    if len(current) >= 4 and target not in ans:
        for ele in current:
            target += ele
        if target not in ans and target in lst:
            ans.append(target)
            print(f'Found: {target}')
            if has_prefix(target):
                search_helper(board, col, row, ans, current, location, target)
        return ans

    elif len(current) == 0:
        for i in range(1, 5, 1):
            for j in range(1, 5, 1):
                # choose
                current.append(board[(i, j)])
                location.append((i, j))

                # explore
                search_helper(board, i, j, ans, current, location, target)

                # un-choose
                current.pop()
                location.pop()
        return ans

    else:
        # choose
        for a in [-1, 0, 1]:
            for b in [-1, 0, 1]:
                if 0 < col + a < 5 and 0 < row + b < 5 and not (a == b == 0):
                    new_col = col + a
                    new_row = row + b
                    if (new_col, new_row) not in location:
                        current.append(board[(new_col, new_row)])
                        location.append((new_col, new_row))

                        # explore
                        target = ''
                        search_helper(board, new_col, new_row, ans, current, location, target)

                        # un-choose
                        current.pop()
                        location.pop()

        return ans


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    global lst

    count = 0
    for element in lst:
        if element.startswith(sub_s):
            count += 1
            break
    if count > 0:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
