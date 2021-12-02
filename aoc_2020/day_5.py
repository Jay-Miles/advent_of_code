#!usr/bin/env python

#5TH DECEMBER
#day5_input.txt
#Input is a list of seat numbers in the form XXXXXXXYYY. X can be F (front) or B (back), and Y can be R (right) or L (left).
#There are 128 rows, each with 8 seats. The 7 X characters specify the row through binary space partitioning. Similarly, the 3 Y characters specify the seat within the row.
#Each seat has a unique ID is equal to ((row number * 8) + seat number)
#There are 867 seat numbers. Each line is 10 characters long, but all except the last have an additional newline character at the end

#Part 1: What is the highest unique ID for the listed seats? Answer: 880 
#Part 2: Identify your plane seat by eliminating all the seats in the input list. Anser: 731

#Read input
with open ('day5_input.txt', 'r') as advent_object:
    advent = advent_object.readlines()
    for line in advent:
        line.strip()

    #Determine the details associated with each seat and store them as dictionaries with the keys 'line', 'row', 'seat' and 'ID'
    all_line_details = []
    curr_line = 1
    for line in advent:
        line_dict = {}
        line_dict['line'] = curr_line
        #Determine row number
        row_range = list(range(0, 128))
        for i in range(0,7):
            if line[i] == 'F':
                row_range = row_range[:(int(len(row_range)/2))]
            elif line[i] == 'B':
                row_range = row_range[(int(len(row_range)/2)):]
        #Determine seat number
        seat_range = list(range(0, 8))
        for j in range(7,10):
            if line[j] == 'L':
                seat_range = seat_range[:(int(len(seat_range)/2))]
            elif line[j] == 'R':
                seat_range = seat_range[(int(len(seat_range)/2)):]
        #Populate the line's dictionary and calculate the seat ID
        line_dict['row'] = row_range[0]
        line_dict['seat'] = seat_range[0]
        line_dict['ID'] = (row_range[0] * 8) + seat_range[0]                        
        all_line_details.append(line_dict)
        curr_line += 1 

    #Determine the highest unique seat ID
    id_max = 0
    for line in all_line_details:
        if line['ID'] > id_max:
            id_max = line['ID']
    print('The highest seat ID is ' + str(id_max))

    #Find the seat IDs either side of yours (1 above and 1 below)
    all_IDs = [] #get a sorted list of all seat IDs
    for dct in all_line_details:
        all_IDs.append(dct['ID'])
    all_IDs.sort()

    curr_ind = 0 #find the seat IDs above and below the missing one (yours)
    for ID in all_IDs:
        try:
            if (all_IDs[curr_ind + 1]) == (ID + 2):
                lower_bound = ID
        except IndexError:
            continue
        try:
            if (all_IDs[curr_ind - 1]) == (ID - 2):
                upper_bound = ID
        except IndexError:
            continue
        curr_ind += 1
    
    if lower_bound == (upper_bound - 2):
        print('Your seat ID is ' + str(upper_bound - 1))
