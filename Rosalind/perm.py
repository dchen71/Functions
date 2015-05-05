#Counts the total number of permutations of length as well as return the list of permutations

import itertools

#Finds and returns the number of permuations and combinations an array has
def perm(n):
	answer = []
	array  = []
	for i in range(1, n +1):
		array.append(i)
	array = itertools.permutations(array)

	for i in array:
		word = ""
		for j in i: #each number of the returned array
			word += str(j) + " "
		word = word[:-1] #remove the last space
		answer.append(word)

	return answer

'''
#Moves the characters over one unit in an array
def rollover(array):
	moved = array
	if len(array) > 1:
		temp0 = array[0]

	for i in range(len(array) - 1):
		temp = moved[i + 1]
		moved[i] = temp
	
	if(len(array) > 1):
		moved[len(moved) - 1] = temp0

	return moved
'''

	
n = 7
answer = perm(n)

#Prints all the uniques
for i in answer:
	print(i)

#Gets the length
print(len(answer))
