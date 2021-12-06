#!usr/bin/env python

"""
PART 1

The submarine has been making some odd creaking noises, so you ask it to
produce a diagnostic report just in case. The diagnostic report
(your puzzle input) consists of a list of binary numbers which, when decoded
properly, can tell you many useful things about the conditions of the
submarine. The first parameter to check is the power consumption.

You need to use the binary numbers in the diagnostic report to generate two
new binary numbers (called the gamma rate and the epsilon rate). The power
consumption can then be found by multiplying the gamma rate by the epsilon
rate.

Each bit in the gamma rate can be determined by finding the most common bit
in the corresponding position of all numbers in the diagnostic report. Take
the example list of binary numbers. Considering only the first bit of each
number, there are five 0 bits and seven 1 bits. Since the most common bit is
1, the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic report is 0, so
the second bit of the gamma rate is 0. The most common value of the third,
fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three
bits of the gamma rate are 110. So, the gamma rate is the binary number
10110, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use the most
common bit, the least common bit from each position is used. So, the epsilon
rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the
epsilon rate (9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate
and epsilon rate, then multiply them together. What is the power consumption
of the submarine? (Be sure to represent your answer in decimal, not binary.)

PART 2

Next, you should verify the life support rating, which can be determined by
multiplying the oxygen generator rating by the CO2 scrubber rating.

Both the oxygen generator rating and the CO2 scrubber rating are values that
can be found in your diagnostic report - finding them is the tricky part.
Both values are located using a similar process that involves filtering out
values until only one remains. Before searching for either rating value,
start with the full list of binary numbers from your diagnostic report and
consider just the first bit of those numbers. Then:

Keep only numbers selected by the bit criteria for the type of rating value
for which you are searching. Discard numbers which do not match the bit
criteria.
If you only have one number left, stop; this is the rating value for which
you are searching.
Otherwise, repeat the process, considering the next bit to the right.
The bit criteria depends on which type of rating value you want to find:

To find oxygen generator rating, determine the most common value (0 or 1) in
the current bit position, and keep only numbers with that bit in that
position. If 0 and 1 are equally common, keep values with a 1 in the
position being considered.
To find CO2 scrubber rating, determine the least common value (0 or 1) in
the current bit position, and keep only numbers with that bit in that
position. If 0 and 1 are equally common, keep values with a 0 in the
position being considered.

Example values:
oxygen generator rating = 23
CO2 scrubber rating = 10
product = 230

Use the binary numbers in your diagnostic report to calculate the oxygen
generator rating and CO2 scrubber rating, then multiply them together. What
is the life support rating of the submarine? (Be sure to represent your
answer in decimal, not binary.)
"""


import argparse


def get_input(input_file):

    with open(input_file, 'r') as file_object:
        file_contents = file_object.readlines()

    binary_numbers = [line.strip() for line in file_contents]

    return binary_numbers


def get_gamma_and_epsilon(binary_numbers):

    binary_gamma_rate = ''
    binary_epsilon_rate = ''

    position_strings = []

    for position in range(len(binary_numbers[0])):
        position_strings.append('')

    for line in binary_numbers:
        for position in range(len(position_strings)):
            position_strings[position] += line[position]

    for position in position_strings:
        count_0 = position.count('0')
        count_1 = position.count('1')

        if count_0 > count_1:
            binary_gamma_rate += '0'
            binary_epsilon_rate += '1'

        elif count_0 < count_1:
            binary_gamma_rate += '1'
            binary_epsilon_rate += '0'

    gamma_rate = int(binary_gamma_rate, 2)
    epsilon_rate = int(binary_epsilon_rate, 2)

    print('gamma rate: {a}\nepsilon rate: {b}'.format(
        a=gamma_rate,
        b=epsilon_rate
        ))

    output_value = gamma_rate * epsilon_rate

    return output_value


def get_o2_and_co2(binary_numbers):

    oxygen_list = binary_numbers
    co2_list = binary_numbers

    string_length = len(binary_numbers[0])

    for position in range(string_length):

        oxygen_string = ''
        for element in oxygen_list:
            oxygen_string += element[position]

        if (oxygen_string.count('0') > oxygen_string.count('1')) and \
            (len(oxygen_list) > 1):

            oxygen_list = [
                element for element in oxygen_list if element[position] == '0'
                ]

        elif ((oxygen_string.count('1') > oxygen_string.count('0')) or \
            (oxygen_string.count('1') == oxygen_string.count('0'))) and \
            (len(oxygen_list) > 1):

            oxygen_list = [
                element for element in oxygen_list if element[position] == '1'
                ]

        co2_string = ''
        for element in co2_list:
            co2_string += element[position]

        if (co2_string.count('0') > co2_string.count('1')) and \
            (len(co2_list) > 1):

            co2_list = [
                element for element in co2_list if element[position] == '1'
                ]

        elif ((co2_string.count('1') > co2_string.count('0')) or \
            (co2_string.count('1') == co2_string.count('0'))) and \
            (len(co2_list) > 1):

            co2_list = [
                element for element in co2_list if element[position] == '0'
                ]

    if (len(oxygen_list) == 1) and (len(co2_list) == 1):
        oxygen = int(oxygen_list[0], 2)
        co2 = int(co2_list[0], 2)

        output_value = oxygen * co2
        return output_value

    else:
        print('Something went wrong.')
        print('oxygen_list: {a}'.format(a=oxygen_list))
        print('co2_list: {a}'.format(a=co2_list))


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    input_file = args.input_file
    binary_numbers = get_input(input_file)

    #output_value = get_gamma_and_epsilon(binary_numbers)
    output_value = get_o2_and_co2(binary_numbers)

    print(output_value)


if __name__ == '__main__':
    main()
