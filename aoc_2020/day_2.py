#!/usr/bin/env python

#2ND DECEMBER
#day2_input.txt
#Each line describes a password and its requirements in the form 'X-Y A: password'. There are 1000 passwords.

#Part 1: A must appear in the password at least X and at most Y times. How many passwords are valid? Answer: 515
#Part 2: A must appear at EITHER position X OR position Y. How many passwords are valid? Answer: 711

with open ('day2_input.txt', 'r') as advent_object_2:
    advent = advent_object_2.readlines()
    print('There are ' + str(len(advent)) + ' passwords')
    line_no = 1
    no_valid = 0
    for line in advent:
        sections = line.split(':')
        password = sections[1].strip()
        requirements = sections[0].split()
        A = requirements[1].strip()
        limits = requirements[0].split('-')
        X = int(limits[0].strip())
        Y = int(limits[1].strip())
        print('X=' + str(X) + '; Y=' + str(Y) + '; A=' + str(A) + '; password = ' + password)
        count = int(password.count(A)) #part1
        if (count >= X) and (count <=Y): #part1
        #if ((password[X-1] == A) and (password[Y-1] != A)) or ((password[Y-1] == A) and (password[X-1] != A)): #part2
            #print('Line ' + str(line_no) + ': ' + line) #part2
            #no_valid += 1 #part2
        line_no +=1
    print('There are ' + str(no_valid) + ' valid passwords')
