#!usr/bin/env python

"""

"""


import argparse


def get_input(input_file):

    with open(input_file, 'r') as file_object:
        file_contents = file_object.readlines()

    data_to_analyse = 

    return data_to_analyse


def some_function(data_to_analyse):

    output_value = 

    return output_value


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    input_file = args.input_file
    data_to_analyse = get_input(input_file)
    output_value = some_function(data_to_analyse)

    print(output_value)


if __name__ == '__main__':
    main()
