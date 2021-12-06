#!usr/bin/env python

"""
PART 1

Now, you need to figure out how to pilot this thing. It seems like the
submarine can take a series of commands like forward 1, down 2, or up 3:

forward X increases the horizontal position by X units.
down X increases the depth by X units.
up X decreases the depth by X units.

Note that since you're on a submarine, down and up affect your depth, and so
they have the opposite result of what you might expect.

The submarine seems to already have a planned course (your puzzle input).
You should probably figure out where it's going. Calculate the horizontal
position and depth you would have after following the planned course. What
do you get if you multiply your final horizontal position by your final
depth?

PART 2

Based on your calculations, the planned course doesn't seem to make any
sense. You find the submarine manual and discover that the process is
actually slightly more complicated.

In addition to horizontal position and depth, you'll also need to track a
third value, aim, which also starts at 0. The commands also mean something
entirely different than you first thought:

down X increases your aim by X units.
up X decreases your aim by X units.
forward X does two things:
It increases your horizontal position by X units.
It increases your depth by your aim multiplied by X.

Using this new interpretation of the commands, calculate the horizontal
position and depth you would have after following the planned course. What
do you get if you multiply your final horizontal position by your final
depth?

"""


import argparse


def get_input(input_file):

    with open(input_file, 'r') as file_object:
        file_contents = file_object.readlines()

    instructions_list = []

    for line in file_contents:
        line_contents = line.split(' ')
        instructions_list.append((line_contents[0], int(line_contents[1])))

    return instructions_list


def find_position(instructions_list):

    horizontal = 0
    depth = 0
    aim = 0

    for tuple in instructions_list:
        if tuple[0] == 'forward':
            horizontal += tuple[1]
            depth += (tuple[1] * aim)

        elif tuple[0] == 'down':
            aim += tuple[1]

        elif tuple[0] == 'up':
            aim -= tuple[1]

    output_value = horizontal * depth

    return output_value


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    input_file = args.input_file
    instructions_list = get_input(input_file)
    output_value = find_position(instructions_list)

    print(output_value)


if __name__ == '__main__':
    main()
