#!/usr/bin/env python

#cd Documents/Advent_of_code

#ADVENT OF CODE
#9TH DECEMBER
#day9_input.txt

#There are 1000 lines, each line is an integer
#The first 25 numbers are a preamble. After that, each number must be a sum of 2 of the preceding 25 numbers.

#Part 1: What is the first number that is NOT a sum of 2 of the preceding 25 numbers? Answer: 
#Part 2:  Answer: 

with open ('day9_input.txt','r') as advent_object:
    advent = advent_object.readlines()
    
    advent_nums = []
    for line in advent:
        number = int(line.strip())
        advent_nums.append(number)
    
    index = 0
    for element in advent_nums[25:]:
        preamble = advent_nums[index:index+25]
        hold1 = 0
        hold2 = 0
        for num1 in preamble:
            for num2 in preamble:
                if num1 + num2 == element:
                    hold1 = num1
                    hold2 = num2
                    continue
        if (hold1 != 0) and (hold2 != 0):
            index += 1
            continue
        else:
            print(index, advent_nums[index])
            print(index+1, advent_nums[index+1])
            break

#536211986 is too low