#Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).
#Return: All strings of length n that can be formed from the alphabet, ordered lexicographically.

import itertools

def organizedstring(string, length):
	#break down string and remove the spaces between char
	#permutations directly should work
	nucleotides = string.replace(" ", "")
	answer  = []
	
	answer = itertools.permutations(nucleotides, 2)
	#none of the itertools can accurately pull it off, need to make a algorithm to do it

	for i in answer:
		print(i)

	return answer

sample = "T A G C"
k = 2
print(organizedstring(sample,k))