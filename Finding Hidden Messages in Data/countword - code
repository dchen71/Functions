import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

#Counts the number of times a pattern is detected
def PatternCount(text, pattern):
	count = 0
	correct = 0

	#loops through the text and matches pattern character by character
	for i in range(len(text) - len(pattern) + 1):
		for j in range(len(pattern)):
			if(text[j + i] == pattern[j]):
				correct += 1
			
		if correct == len(pattern):
			count += 1
			correct = 0
			i += len(pattern) - 1
		else:
			correct = 0
		
		
	return count

input = str(lines[0])
check = str(lines[1])


print(PatternCount(input,check))
