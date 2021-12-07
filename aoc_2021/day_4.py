#!usr/bin/env python

"""
PART 1

You're already almost 1.5km (almost a mile) below the surface of the ocean,
already so deep that you can't see any sunlight. What you can see, however,
is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo? Bingo is played on a set of boards each
consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the
chosen number is marked on all boards on which it appears. (Numbers may not
appear on all boards.) If all numbers in any row or any column of a board
are marked, that board wins. (Diagonals don't count.)

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
winners. After the next six numbers are drawn (17, 23, 2, 0, 14, and 21),
there are still no winners. Finally, 24 is drawn. At this point, the third
board wins because it has at least one complete row or column of marked
numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the
sum of all unmarked numbers on that board; in this case, the sum is 188.
Then, multiply that sum by the number that was just called when the board
won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will
win first. What will your final score be if you choose that board?

PART 2

On the other hand, it might be wise to try a different strategy: let the
giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so
rather than waste time counting its arms, the safe thing to do is to figure
out which board will win last and choose that one. That way, no matter which
boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens
after 13 is eventually called and its middle column is completely marked. If
you were to keep playing until this point, the second board would have a sum
of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final
score be?
"""


import argparse


def get_input(input_file):

    with open(input_file, 'r') as file_object:
        file_contents = file_object.read()

    first_return = file_contents.find('\n')

    draw_string = file_contents[:first_return]
    draw_list = draw_string.split(',')
    draw_numbers = [element.strip() for element in draw_list if element.strip() != '']

    boards_string = (file_contents[first_return:]).split('\n')
    list_of_rows = [element for element in boards_string if element.strip() != '']
    no_of_rows = len(list_of_rows)
    list_of_boards = []

    for i in range(0, no_of_rows, 5):
        board = []
        rows = list_of_rows[i : i+5]

        for row in rows:
            numbers = [number.strip() for number in row.split(' ') if number.strip() != '']
            board.append(numbers)

        list_of_boards.append(board)

    # print(draw_numbers)
    # print('There are {a} boards:'.format(a=len(list_of_boards)))
    # print(list_of_boards)

    return draw_numbers, list_of_boards


def find_the_winner(draw_numbers, list_of_boards):

    modified_boards = list_of_boards

    for number in draw_numbers:
        for board in list_of_boards:
            board_index = list_of_boards.index(board)

            for row in board:
                row_index = board.index(row)

                if number in row:
                    number_index = row.index(number)
                    modified_boards[board_index][row_index][number_index] = 'x'

                if modified_boards[board_index][row_index] == ['x', 'x', 'x', 'x', 'x']:
                    winning_board = board
                    last_number = number

                    return last_number, winning_board

            for i in range(0, 5, 1):
                column = [row[i] for row in board]
                if column == ['x', 'x', 'x', 'x', 'x']:
                    winning_board = board
                    last_number = number

                    return last_number, winning_board


def winning_output(last_number, winning_board):

    sum_of_remaining_numbers = 0
    for row in winning_board:
        for element in row:
            if element != 'x':
                sum_of_remaining_numbers += int(element)

    output_value = sum_of_remaining_numbers * int(last_number)

    return output_value


def find_last_winner(draw_numbers, list_of_boards):

    modified_boards = list_of_boards.copy()

    for number in draw_numbers:
        for board in list_of_boards:
            if board == 'board has won already':
                continue

            board_index = list_of_boards.index(board)
            for row in board:
                row_index = board.index(row)

                if number in row:
                    number_index = row.index(number)
                    modified_boards[board_index][row_index][number_index] = 'x'

                    if modified_boards[board_index][row_index] == ['x', 'x', 'x', 'x', 'x']:
                        most_recent_number = number
                        most_recent_board = modified_boards[board_index]
                        list_of_boards[board_index] = 'board has won already'

                    for i in range(0, 5, 1):
                        column = [row[i] for row in board]
                        if column == ['x', 'x', 'x', 'x', 'x']:
                            most_recent_number = number
                            most_recent_board = modified_boards[board_index]
                            list_of_boards[board_index] = 'board has won already'

    print('last number to win: {a}'.format(a=most_recent_number))
    print('last board to win: {a}'.format(a=most_recent_board))

    sum_of_remaining_numbers = 0
    for row in most_recent_board:
        for element in row:
            if element != 'x':
                sum_of_remaining_numbers += int(element)

    output_value = sum_of_remaining_numbers * int(most_recent_number)

    return output_value


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    input_file = args.input_file
    draw_numbers, list_of_boards = get_input(input_file)
    #last_number, winning_board = find_the_winner(draw_numbers, list_of_boards)
    #output_value = winning_output(last_number, winning_board)
    output_value = find_last_winner(draw_numbers, list_of_boards)

    print(output_value)


if __name__ == '__main__':
    main()
