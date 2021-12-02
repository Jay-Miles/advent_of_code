#!usr/bin/env python

#4TH DECEMBER
#day4_input.txt
#Part 1: Each entry contains up to 8 key:value fields. An entry is valid if all 8 are present or if only the 'cid' field is missing. How many entries are valid? Answer: 210
#Part 2: There are now also restrictions on which values are valid in each field (below). How many entries are still valid? Answer: 131

#Read the input
with open('day4_input.txt', 'r') as advent_object_4:
    advent = advent_object_4.readlines()
    for line in advent:
        line.strip()
    print('The original file has ' + str(len(advent)) + ' lines.')

    #Condense each entry into a single line
    curr_line = 0
    for line in advent: #get all information for an entry into the entry's last line, and change the other lines to just say 'DELETE' (unless they're blank, in which case ignore them)
        if curr_line < (len(advent)-1):
            if advent[curr_line + 1] != '\n':
                advent[curr_line + 1] += (' ' + advent[curr_line])
                advent[curr_line] = 'DELETE'
        curr_line += 1
    for i in range(len(advent)): #remove all the lines which just say 'DELETE'
        curr_line = 0
        for line in advent:
            if line == 'DELETE':
                del advent[curr_line]
            curr_line += 1

    #Create a list of 276 dictionaries (one per entry) by converting each line into a dictionary
    line_no = 1
    lst_line_dicts = []
    for line in advent: #create a list of elements split by spaces (i.e. 'a:b c:d e:f' -> 'a:b','c:d','e:f')
        #print(line)
        line_dict = {}
        if line != '\n':
            line_list = line.split(' ')
            if line_list[-1] == '\n':
                del line_list[-1]
            #print(line_list)
            for element in line_list: #for each element, split it at the colon and use the two strings as a dictionary entry (i.e. 'a:b' -> 'a', 'b')
                elem_list = element.split(':')
                line_dict[elem_list[0]] = elem_list[1]
            for key, value in line_dict.items(): #remove any newline characters from dictionary values
                line_dict[key] = value.replace('\n','')
            line_no += 1
        else:
            line_no += 1
        lst_line_dicts.append(line_dict)            

    #Add valid entries (based on fields present) to a new list
    valid_list = []
    valid_entries = 0
    for line in lst_line_dicts:
        if len(line.values()) == 8:
            valid_list.append(line)
            valid_entries += 1
        elif (len(line.values()) == 7) and ('cid' not in line):
            valid_list.append(line)
            valid_entries += 1
    print('There are ' + str(valid_entries) + ' valid entries. The valid list is ' + str(len(valid_list)) + ' entries long.')   #the two numbers should match

    #Add valid entries (based on field values below) to a new list
    #byr (Birth Year) - four digits; at least 1920 and at most 2002
    #iyr (Issue Year) - four digits; at least 2010 and at most 2020
    #eyr (Expiration Year) - four digits; at least 2020 and at most 2030
    #hgt (Height) - a number followed by either cm or in:
    #   If cm, the number must be at least 150 and at most 193
    #   If in, the number must be at least 59 and at most 76
    #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f
    #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth
    #pid (Passport ID) - a nine-digit number, including leading zeroes

    hcl_ops = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']  #in form '#' + 6 characters from 0-9 or a-f
    ecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] #can only have one value
    pids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    final_list = []
    final_count = 0
    curr_line = 1
    for line in valid_list:
        line_points = 0
        if ('byr' in line.keys()) and (1920 <= int(line['byr']) <= 2002) and ((len(line['byr'])) == 4):
            line_points += 1
        if ('iyr' in line.keys()) and (2010 <= int(line['iyr']) <= 2020) and ((len(line['iyr'])) == 4):
            line_points += 1
        if ('eyr' in line.keys()) and (2020 <= int(line['eyr']) <= 2030) and ((len(line['eyr'])) == 4):
            line_points += 1
        if ('hgt' in line.keys()) and (((line['hgt'][-2:] == 'cm') and (150 <= float(line['hgt'][:-2]) <= 193)) or ((line['hgt'][-2:] == 'in') and (59 <= float(line['hgt'][:-2]) <= 76))):
            line_points += 1
        if ('hcl' in line.keys()) and (line['hcl'][0] == '#') and ((len(line['hcl'])) == 7) and (char in hcl_ops for char in line['hcl']):
            line_points += 1
        if ('ecl' in line.keys()) and (line['ecl'] in ecls):
            line_points += 1
        if ('pid' in line.keys()) and ((len(line['pid'])) == 9) and (char in pids for char in line['pid']):
            line_points += 1

        if line_points == 7:
            final_list.append(line)
            final_count += 1
        curr_line += 1
    
    print('There are ' + str(final_count) + ' REALLY valid passwords.')
