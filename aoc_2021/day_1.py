#!usr/bin/env python

"""
PART 1

As the submarine drops below the surface of the ocean, it automatically
performs a sonar sweep of the nearby sea floor. On a small screen, the sonar
sweep report (your puzzle input) appears: each line is a measurement of the
sea floor depth as the sweep looks further and further away from the
submarine.

The first order of business is to figure out how quickly the depth
increases, just so you know what you're dealing with - you never know if the
keys will get carried into deeper water by an ocean current or a fish or
something.

To do this, count the number of times a depth measurement increases from the
previous measurement. (There is no measurement before the first
measurement.) How many measurements are larger than the previous one?

PART 2

Considering every single measurement isn't as useful as you expected:
there's just too much noise in the data. Instead, consider sums of a
three-measurement sliding window.

Your goal now is to count the number of times the sum of measurements in
this sliding window increases from the previous sum. So, compare A with B,
then compare B with C, then C with D, and so on. Stop when there aren't
enough measurements left to create a new three-measurement sum.

Consider sums of a three-measurement sliding window. How many sums are
larger than the previous sum?

"""


import argparse


def get_input(input_file):

    with open(input_file, 'r') as file_object:
        file_contents = file_object.readlines()

    list_of_depths = [int(element) for element in file_contents]

    return list_of_depths


def basic_increases(list_of_depths):

    output_value = 0

    for i in range(len(list_of_depths)):
        if list_of_depths[i] > list_of_depths[i-1]:
            output_value += 1

    return output_value


def sliding_increases(list_of_depths):

    window_sums = []

    for i in range(len(list_of_depths)):
        try:
            window_sum = list_of_depths[i] + list_of_depths[i+1] + list_of_depths[i+2]
            window_sums.append(window_sum)

        except IndexError:
            continue

    print(window_sums)

    output_value = 0

    for i in range(len(window_sums)):
        if window_sums[i] > window_sums[i-1]:
            output_value += 1

    return output_value


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    input_file = args.input_file
    list_of_depths = get_input(input_file)

    # output_value = basic_increases(list_of_depths)
    output_value = sliding_increases(list_of_depths)

    print(output_value)


if __name__ == '__main__':
    main()
