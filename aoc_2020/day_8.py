#!/usr/bin/env python

#cd Documents/Advent_of_code

#ADVENT OF CODE
#8TH DECEMBER
#day8_input.txt

#The file consists of 656 lines, which are instructions comprised of acc (accumulator), jmp (jump) and nop (no operation) operations plus a numerical argument
# acc: The accumulator value (starts at 0) is modified by the value of the argument. The line immediately below is executed next.
# jmp: The next line to be executed is specified by the argument relative to the current line.
# nop: Does nothing. The line immediately below is executed next.

#Part 1: Currently the file is an infinite loop. Before any line gets executed a second time, what is the accumulator value? Answer: 1594
#Part 2: Fix the file by changing one 'jmp' to a 'nop' or one 'nop' to a 'jmp'. What is the accumulator? Answer: 

with open ('day8_input.txt','r') as advent_object:
    advent = advent_object.readlines()

    #Turn each line into a list of ['operator', argument, times executed]
    index = 0
    for line in advent:
        newLine = (line.strip()).split(' ')
        newArg = int(newLine[1])
        advent[index] = [newLine[0], newArg, 0]
        index += 1
    
    #Define a function which executes lines until it's about to repeat one
    def run_loop():
        accumulator = 0
        index = 0
        executes = 0
        while advent[index][2] < 1:
            if advent[index][0] == 'acc':
                #print('acc = ' + str(accumulator) + '; index = ' + str(index) + '; executes = ' + str(executes))
                accumulator += advent[index][1]
                advent[index][2] += 1
                index += 1
                executes += 1
            elif advent[index][0] == 'jmp':
                #print('acc = ' + str(accumulator) + '; index = ' + str(index) + '; executes = ' + str(executes))
                advent[index][2] += 1            
                index += advent[index][1]
                executes += 1
            elif advent[index][0] == 'nop':
                #print('acc = ' + str(accumulator) + '; index = ' + str(index) + '; executes = ' + str(executes))
                advent[index][2] += 1
                index += 1
                executes += 1
        print('accumulator: ' + str(accumulator))
        return accumulator

    #print(run_loop())

    for line in advent:
        if line[0] == 'jmp':
            try:
                line[0] == 'nop'
                run_loop()
            except advent[index][2] > 1:
                continue
        elif line[0] == 'nop':
            try:
                line[0] == 'jmp'
                run_loop()
            except advent[index][2] > 1:
                continue

#0 and 87 are wrong