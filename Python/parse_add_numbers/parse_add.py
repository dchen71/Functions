# Parses text files and returns the sum of the numeric values.

import re

def parse_add(filename):
    f = open(filename, 'r')
    total = 0
    for line in f:
    	line = line.rstrip()
    	numbers = re.findall('[0-9]+',line)
    	print(numbers)
    	for i in numbers:
    		total += int(i)
    print(total)
    return total

'''
#Tests
name = "regex_sum_42.txt"
total = parse_add(name)
assert(total) == 445822


name = "regex_sum_169145.txt"
total = parse_add(name)
assert(total) == 392282
'''
