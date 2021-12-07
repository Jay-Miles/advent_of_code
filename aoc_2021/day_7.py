#!usr/bin/env python

"""
A giant whale has decided your submarine is its next meal, and it's much
faster than you are. There's nowhere to run! Suddenly, a swarm of crabs
(each in its own tiny submarine - it's too deep for them otherwise) zooms in
to rescue you! They seem to be preparing to blast a hole in the ocean floor;
sensors indicate a massive underground cave system just beyond where they're
aiming!

The crab submarines all need to be aligned before they'll have enough power
to blast a large enough hole for your submarine to get through. However, it
doesn't look like they'll be aligned before the whale catches you! Maybe you
can help?

There's one major catch - crab submarines can only move horizontally. You
quickly make a list of the horizontal position of each crab (your puzzle
input). Crab submarines have limited fuel, so you need to find a way to make
all of their horizontal positions match while requiring them to spend as
little fuel as possible.

For example, consider the following horizontal positions:
16,1,2,0,4,2,7,1,2,14
This means there's a crab with horizontal position 16, a crab with
horizontal position 1, and so on.

Each change of 1 step in horizontal position of a single crab costs 1 fuel.
You could choose any horizontal position to align them all on, but the one
that costs the least fuel is horizontal position 2 which costs a total of 37
fuel.

Determine the horizontal position that the crabs can align to using the
least fuel possible. How much fuel must they spend to align to that
position?

PART 2

The crabs don't seem interested in your proposed solution. Perhaps you
misunderstand crab engineering? As it turns out, crab submarine engines
don't burn fuel at a constant rate. Instead, each change of 1 step in
horizontal position costs 1 more unit of fuel than the last: the first step
costs 1, the second step costs 2, the third step costs 3, and so on.

As each crab moves, moving further becomes more expensive. This changes the
best horizontal position to align them all on; in the example above, this
becomes 5 costing a total of 168 fuel.

Determine the horizontal position that the crabs can align to using the
least fuel possible so they can make you an escape route! How much fuel must
they spend to align to that position?
"""


import argparse


def get_input(input_file):

    with open(input_file, 'r') as file_object:
        file_contents = file_object.read()

    contents_list = file_contents.split(',')

    data_to_analyse = [int(element) for element in contents_list]

    return data_to_analyse


def optimise_crab_positions(data_to_analyse):

    biggest_move = max(data_to_analyse)
    biggest_cost = (biggest_move * (biggest_move + 1)) / 2

    best_position = 0
    best_cost = len(data_to_analyse) * biggest_cost

    for current_position in range(0, len(data_to_analyse) + 1):

        list_of_costs = []

        for crab_position in data_to_analyse:

            distance_to_move = (
                max(current_position, crab_position) - \
                min(current_position, crab_position)
                )

            cost_to_move = (distance_to_move * (distance_to_move + 1)) / 2
            list_of_costs.append(cost_to_move)

        if sum(list_of_costs) < best_cost:
            best_cost = sum(list_of_costs)
            best_position = current_position

    return best_position, best_cost


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    input_file = args.input_file
    data_to_analyse = get_input(input_file)
    best_position, best_cost = optimise_crab_positions(data_to_analyse)

    print('best position to take: {a}'.format(a=best_position))
    print('cost for this position: {a}'.format(a=best_cost))


if __name__ == '__main__':
    main()
