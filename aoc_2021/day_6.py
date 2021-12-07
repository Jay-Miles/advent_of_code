#!usr/bin/env python

# PART 2 INCOMPLETE - MEMORY OPTIMISATION PROBLEM

"""
PART 1

The sea floor is getting steeper. Maybe the sleigh keys got carried this
way? A massive school of glowing lanternfish swims past. They must spawn
quickly to reach such large numbers - maybe exponentially quickly? You
should model their growth rate to be sure.

Although you know nothing about this specific species of lanternfish, you
make some guesses about their attributes. Surely, each lanternfish creates a
new lanternfish once every 7 days. However, this process isn't necessarily
synchronized between every lanternfish - one lanternfish might have 2 days
left until it creates another lanternfish, while another might have 4. So,
you can model each fish as a single number that represents the number of
days until it creates a new lanternfish.

Furthermore, you reason, a new lanternfish would surely need slightly longer
before it's capable of producing more lanternfish: two more days for its
first cycle.

So, suppose you have a lanternfish with an internal timer value of 3:

After one day, its internal timer would become 2.
After another day, its internal timer would become 1.
After another day, its internal timer would become 0.
After another day, its internal timer would reset to 6, and it would create
a new lanternfish with an internal timer of 8.
After another day, the first lanternfish would have an internal timer of 5,
and the second lanternfish would have an internal timer of 7.
A lanternfish that creates a new fish resets its timer to 6, not 7 (because
0 is included as a valid timer value). The new lanternfish starts with an
internal timer of 8 and does not start counting down until the next day.

Realizing what you're trying to do, the submarine automatically produces a
list of the ages of several hundred nearby lanternfish (your puzzle input).
For example, suppose you were given the following list:

3,4,3,1,2

This list means that the first fish has an internal timer of 3, the second
fish has an internal timer of 4, and so on until the fifth fish, which has
an internal timer of 2.

Each day, a 0 becomes a 6 and adds a new 8 to the end of the list, while
each other number decreases by 1 if it was present at the start of the day.

In this example, after 18 days, there are a total of 26 fish. After 80 days,
there would be a total of 5934.

Find a way to simulate lanternfish. How many lanternfish would there be
after 80 days?

PART 2

Suppose the lanternfish live forever and have unlimited food and space.
Would they take over the entire ocean?

After 256 days in the example above, there would be a total of 26984457539
lanternfish!

How many lanternfish would there be after 256 days?
"""


import argparse


def get_input(input_file):

    with open(input_file, 'r') as file_object:
        file_contents = file_object.read()

    contents_list = file_contents.split(',')

    data_to_analyse = [int(element) for element in contents_list]

    return data_to_analyse


def model_lanternfish(data_to_analyse):

    progression = {0 : data_to_analyse}

    for i in range(1, 257):

        yesterdays_fish = progression[i-1]
        todays_fish = []

        for fish in yesterdays_fish:
            if fish > 0:
                todays_fish.append(fish-1)

            elif fish == 0:
                todays_fish.append(6)
                todays_fish.append(8)

        progression[i] = todays_fish
        del progression[i-1]

        print('day {a}: {b} fish'.format(a=i, b=len(progression[i])))

    output_value = len(progression[256])

    return output_value


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    input_file = args.input_file
    data_to_analyse = get_input(input_file)
    output_value = model_lanternfish(data_to_analyse)

    print(output_value)


if __name__ == '__main__':
    main()
