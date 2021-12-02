#!usr/bin/env python

#6TH DECEMBER
#day6_input.txt
#Each line is a combination of letters a-z, of varying lengths. Adjacent lines which are not separated by a blank line are in the same group.
#There are 2232 lines, 497 are blank (so there should be 498 groups)

#Part 1: Within each group, identify how many unique letters appear. Sum this for all groups. Answer: 6662
#Part 2: Within each group, identify how many unique letters appear in all of the group's lines. Sum this for all groups. Answer: 3382

with open ('day6_input.txt', 'r') as advent_object:
    advent = advent_object.readlines()

    #For each line, remove any duplicate characters or newlines, ensure that all characters are lowercase, and sort alphabetically. Leave blank lines as they are.
    index = 0
    for line in advent:
        (line.strip()).lower()
        line_str = ''
        if line == '\n':
            line_str = '\n'
        else:
            for character in line:
                if (character != '\n') and (character not in line_str):
                    line_str += character
        advent[index] = ''.join(sorted(line_str))
        index += 1

    #Identify the number of lines in each group and store this in a list of dictionaries e.g. [{'group':1, 'lines':2}.......]
    grp_size = 0
    grp_size_list = []
    index = 0
    for line in advent:
        if line == advent[-1]:
            grp_size += 1
            grp_entry = {'group':(index+1), 'lines':grp_size}
            grp_size_list.append(grp_entry)
            grp_size = 0
            index += 1
        elif line != '\n':
            grp_size += 1
        else:
            grp_entry = {'group':(index+1), 'lines':grp_size}
            grp_size_list.append(grp_entry)
            grp_size = 0
            index += 1

    #combine each group's lines into one single line
    index = 0 
    for line in advent:
        try:
            if advent[index+1] != '\n':
                advent[index+1] += advent[index]
                advent[index] = 'DELETE'
        except IndexError:
            continue
        index += 1
    for i in range(len(advent)): 
        index = 0
        for line in advent:
            if line == 'DELETE':
                del advent[index]
            index += 1

    #make a new list with one element per group where all duplicate letters are removed
    no_dups = []
    index = 0
    for group in advent:
        grp_string = ''
        for character in group:
            if (character != '\n') and (character not in grp_string):
                grp_string += character
        condensed = ''.join(sorted(grp_string))
        no_dups.append(condensed)
        index += 1

    #Part 1: find the number of characters in no_dups
    #count = 0
    #for entry in no_dups:
        #count += len(entry)
    #print('There are ' + str(count) + ' characters')

    #Part 2: 
    index = 0
    total_count = 0
    for element in advent:
        common_chars = ''
        for character in element:
            if ((element.strip()).count(character) == grp_size_list[index]['lines']) and (character not in common_chars):
                common_chars += character
        count = len(common_chars)
        total_count += count
        index += 1
    print('Total count is: ' + str(total_count))
