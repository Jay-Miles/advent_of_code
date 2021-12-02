#!/usr/bin/env python

#cd Documents/Advent_of_code

#ADVENT OF CODE
#7TH DECEMBER
#day7_input.txt

#The file describes rules for the numbers and colours of other bags that each colour of bag contains (e.g. 'red bags contain 3 blue bags, 1 green bag.')
#There are 594 lines, each line contains a rule for one bag colour

#Part 1: How many colours of bag can eventually hold a shiny gold bag? Answer: 254
#Part 2: How many other bags does a single shiny gold bag hold? Answer: 

with open ('day7_input.txt','r') as advent_object:
    advent = advent_object.readlines()
    #print('The file is ' + str(len(advent)) + ' lines long')

    #Turn each line into a list of bags (e.g. ['red', '3 blue', '1 green'])
    line_no = 0
    for line in advent: #e.g. 'red bags contain 3 blue bags, 1 green bag.'
        line = (line.replace('.','')).lower()
        line_bags = line.split('bag')
        index = 0
        for bag in line_bags: #e.g. 'red ', 's contain 3 blue ', 's, 1 green '
            bag.strip()
            if bag[:2] == 's ':
                newBag1 = bag[2:]
            elif bag[:3] == 's, ':
                newBag1 = bag[3:]
            else:
                newBag1 = bag
            newBag2 = newBag1.replace('contain','')
            newBag3 = newBag2.replace(',','')
            newBag4 = newBag3.replace('other','')
            line_bags[index] = newBag4.strip()
            if (line_bags[index] == 's') or (line_bags[index] == ''):
                del line_bags[index]
            index += 1
        advent[line_no] = line_bags
        line_no += 1

    #Turn each line into a list of dictionaries e.g. ['red', {'blue':3}, {'green':1}]
    line_no = 0
    for line in advent:
        #print(line)
        line_list = []
        line_list.append(line[0])
        for element in line[1:]:
            #print(element)
            if element == 'no':
                line_list.append({})
            else:               
                first_space = element.find(' ')
                components = [(element[:first_space]).strip(), (element[first_space:]).strip()]
                line_list.append({components[1]:int(components[0])})
        #print(line_list)
        advent[line_no] = line_list
        line_no += 1

    #Part 1: Find lines which contain the string 'shiny gold'
    #hold_gold = []
    #for colour in advent: #identify which colours directly hold a gold bag
        #[hold_gold.append(colour[0]) for element in colour[1:] if ((colour[1] != {}) and (list(element.keys())[0] == 'shiny gold') and (colour[0] not in hold_gold))]
    #for i in range(len(advent)): #iterate through all lines multiple times to determine whether each colour bag holds a bag which could eventually hold a gold bag
        #for colour in advent:
            #[hold_gold.append(colour[0]) for element in colour[1:] if ((colour[1] != {}) and (list(element.keys())[0] in hold_gold) and (colour[0] not in hold_gold))]
    #print('There are ' + str(len(hold_gold)) + ' bag colours')

    #Part 2: How many other bags must a gold bag contain?
    total_bags = 0
    lv0_bag = 'shiny_gold'
    lv0_mult = 1

