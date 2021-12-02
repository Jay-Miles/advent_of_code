#!usr/bin/env python

#3 DECEMBER
#day3_input.txt
#The file is a 31-column, 323-row map of trees (#) and open space (.). The map is theoretically repeated an infinite number of times to left and right.
#NOTE: Awkwardly, although all the lines are definitely 31 characters long, for some reason all except line 322 show as being 32 characters long. I suspect there is an invisible newline character at the end of most of them.

#Part 1: If you start in the top left and move with a gradient of 3 spaces right and 1 down, how many trees are on this line between the first and last lines? Answer: 151
#Part 2: For this and 4 other slopes (1 right, 1 down - 103), (5 right, 1 down - 83), (7 right, 1 down - 99), and (1 right, 2 down - 59), what is the product of all trees hit on all slopes? Answer: 7540141059

#Read input
with open ('day3_input', 'r') as advent_object_3:
    advent = advent_object_3.readlines()
    for line in advent:
        line.strip()
    
    #Set up the starting position, then move across the map
    no_lines = len(advent)
    position = [1,1] #as [row, column]
    trees = 0
    for i in range(no_lines):
        curr_row = position[0]
        curr_col = position[1]
        #print(i, curr_row, curr_col)
        #is there a tree in the current position?
        if curr_row <= no_lines:
            if advent[curr_row-1][curr_col-1] != '.':
                trees += 1
        #move 3 spaces to the right
        if (curr_col + 3) <= 31:
            position[1] += 3
        else:
            position[1] = (curr_col + 3) - 31
        #move 1 space down
        if (curr_row) <= no_lines:
            position[0] += 1
        else:
            break
    
    print('You are at row ' + str(position[0]) + ', column ' + str(position[1]) + '. You hit ' + str(trees) + ' trees.')
