#!usr/bin/env python

"""
PART 1

You're already almost 1.5km (almost a mile) below the surface of the ocean,
already so deep that you can't see any sunlight. What you can see, however,
is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers.
Numbers are chosen at random, and the chosen number is marked on all boards
on which it appears. (Numbers may not appear on all boards.) If all numbers
in any row or any column of a board are marked, that board wins. (Diagonals
don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and
the giant squid) pass the time. It automatically generates a random order in
which to draw numbers and a random set of boards (your puzzle input). For
example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7

After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no
winners, but the boards are marked as follows (shown here adjacent to each
other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are
still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
Finally, 24 is drawn:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

At this point, the third board wins because it has at least one complete row
or column of marked numbers (in this case, the entire top row is marked: 14
21 17 24 4).

The score of the winning board can now be calculated. Start by finding the
sum of all unmarked numbers on that board; in this case, the sum is 188.
Then, multiply that sum by the number that was just called when the board
won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will
win first. What will your final score be if you choose that board?
"""


import argparse


def get_input(input_file):

    with open(input_file, 'r') as file_object:
        file_contents = file_object.read()

    first_return = file_contents.find('\n')

    draw_string = file_contents[:first_return]
    draw_numbers = draw_string.split(',')

    #print(draw_numbers)

    boards_string = (file_contents[first_return:]).split('\n')
    list_of_rows = [element for element in boards_string if element.strip() != '']

    #print(list_of_rows)

    no_of_rows = len(list_of_rows)
    no_of_boards = int(no_of_rows / 5)

    #print('{a} rows from {b} boards'.format(a=no_of_rows, b=no_of_boards))

    list_of_boards = []

    for i in range(0, no_of_rows, 5):

        board = []
        rows = list_of_rows[i : i+5]

        for row in rows:
            numbers = [number.strip() for number in row.split(' ') if number.strip() != '']
            board.append(numbers)

        list_of_boards.append(board)

    #print('{a} boards created'.format(a=len(list_of_boards)))
    #print(list_of_boards[0])

    return list_of_boards


def find_the_winner(list_of_boards):

    output_value = 'not done this yet'

    return output_value


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    input_file = args.input_file
    list_of_boards = get_input(input_file)
    output_value = find_the_winner(list_of_boards)

    print(output_value)


if __name__ == '__main__':
    main()
