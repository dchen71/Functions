#Counts the total number of permutations of length as well as return the list of permutations

import itertools

#Finds and returns the number of permuations and combinations an array has
def perm(n):
	answer = set() #needs to be all unique
	array  = range(1, n + 1) #range list dont seem to work so for loop it*either than or it cause it ints not list

	for i in range(len(array)):
		if i == 0:
			answer.add(itertools.product(array,n))
		else:
			answer.add(itertools.product(rollover(array),n))
	
	#return a formatted answer string

	return answer

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

print(perm(5))