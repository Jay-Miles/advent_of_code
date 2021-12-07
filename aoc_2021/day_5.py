#!usr/bin/env python

"""
PART 1

You come across a field of hydrothermal vents on the ocean floor! These
vents constantly produce large, opaque clouds, so it would be best to avoid
them if possible. They tend to form in lines; the submarine helpfully
produces a list of nearby lines of vents (your puzzle input) for you to
review. Each line of vents is given as a line segment in the format
x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment
and x2,y2 are the coordinates of the other end. These line segments include
the points at both ends. In other words:

An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
For now, only consider horizontal and vertical lines: lines where either
x1 = x2 or y1 = y2.

To avoid the most dangerous areas, you need to determine the number of
points where at least two lines overlap. In the above example, this is
anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least
two lines overlap?

PART 2

Unfortunately, considering only horizontal and vertical lines doesn't give
you the full picture; you need to also consider diagonal lines. Because of
the limits of the hydrothermal vent mapping system, the lines in your list
will only ever be horizontal, vertical, or a diagonal line at exactly 45
degrees. In other words:

An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.

You still need to determine the number of points where at least two lines
overlap. Consider all of the lines. At how many points do at least two lines
overlap?
"""


import argparse


def get_input(input_file):

    with open(input_file, 'r') as file_object:
        file_contents = file_object.readlines()

    data_to_analyse = []

    for line in file_contents:
        line_start, line_end = line.split(' -> ')

        start_x, start_y = line_start.split(',')
        end_x, end_y = line_end.split(',')

        values = (int(start_x), int(end_x), int(start_y), int(end_y))
        data_to_analyse.append(values)

    return data_to_analyse


def create_map(data_to_analyse):

    max_x = 0
    max_y = 0

    for line in data_to_analyse:
        if max(line[:2]) > max_x:
            max_x = max(line[:2])

        if max(line[3:]) > max_y:
            max_y = max(line[3:])

    single_row = []
    for x in range(max_x + 1):
        single_row.append(0)

    map = []
    for y in range(max_y + 1):
        map.append(single_row)

    return map


def populate_map(data_to_analyse, map):

    for line in data_to_analyse:

        # vertical lines
        if line[0] == line[1]:

            start_y = min(line[2:])
            end_y = max(line[2:])

            row_to_add = [0] * len(map[0])
            row_to_add[line[0]] += 1

            for i in range(start_y, end_y + 1):
                try:
                    old_row = map[i]
                    map[i] = [x + y for x, y in zip(old_row, row_to_add)]

                except IndexError:
                    continue

        # horizontal lines
        elif line[2] == line[3]:

            old_row = map[line[2]]
            start_x = min(line[:2])
            end_x = max(line[:2])

            row_to_add = [0] * len(map[0])
            for i in range(start_x, end_x + 1):
                row_to_add[i] += 1

            map[line[2]] = [x + y for x, y in zip(old_row, row_to_add)]

        # diagonal lines left-right
        elif ((line[0] < line[1]) and (line[2] < line[3])) or \
            ((line[0] > line[1]) and (line[2] > line[3])):

            first_row = min(line[2:])
            last_row = max(line[2:])
            first_column = min(line[:2])

            for i in range(0, 1 + last_row - first_row):
                try:
                    old_row = map[first_row + i]

                    row_to_add = [0] * len(old_row)
                    row_to_add[first_column + i] += 1

                    map[first_row + i] = [x + y for x, y in zip(old_row, row_to_add)]

                except IndexError:
                    continue

        # diagonal lines right-left
        elif ((line[0] < line[1]) and (line[2] > line[3])) or \
            ((line[0] > line[1]) and (line[2] < line[3])):

            first_row = min(line[2:])
            last_row = max(line[2:])
            first_column = max(line[:2])

            for i in range(0, 1 + last_row - first_row):
                try:
                    old_row = map[first_row + i]

                    row_to_add = [0] * len(old_row)
                    row_to_add[first_column - i] += 1

                    map[first_row + i] = [x + y for x, y in zip(old_row, row_to_add)]

                except IndexError:
                    continue

    output_value = 0
    for row in map:
        for element in row:
            if element >= 2:
                output_value += 1

    return output_value


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    input_file = args.input_file
    data_to_analyse = get_input(input_file)
    map = create_map(data_to_analyse)
    output_value = populate_map(data_to_analyse, map)

    print(output_value)


if __name__ == '__main__':
    main()
