#!/usr/bin/env python

#1ST DECEMBER
#day1_input.txt
#Each line consists of one integer

#Part 1: Find the two numbers which sum to 2020 and multiply them together. Answer: 270144
#Part 2: Find the three numbers which sum to 2020 and multiply them together. Answer: 261342720

with open ('day1_input.txt', 'r') as advent_object_1:
    advent = advent_object_1.readlines()
    for a in advent:
        A = int(a)
        for b in advent:
            B = int(b)
            if (A + B) == 2020:   #part1
                ansA = A   #part1
                ansB = B   #part1
                break   #part1
            #for c in advent:    #part2
                #C = int(c)    #part2
                #if (A+B+C) == 2020:    #part2
                    #ansA = A    #part2
                    #ansB = B    #part2
                    #ansC = C    #part2
                    #break    #part2
    print('a = ' + str(ansA) + '; b = ' + str(ansB))   #part1
    X = ansA * ansB    #part1
    #print('a = ' + str(ansA) + '; b = ' + str(ansB) + '; c = '+str(ansC))    #part2
    #X = ansA * ansB * ansC    #part2
    print('Answer: '+str(X))