#Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).
#Return: All strings of length n that can be formed from the alphabet, ordered lexicographically.

import itertools

def organizedstring(string, length):
	#break down string and remove the spaces between char
	nucleotides = string.replace(" ", "")
	answer = []

	#pool = tuple(nucleotides) #tuples are immutable list, required if going yield route
	n = len(nucleotides)
	r = length
	for indices in itertools.product(range(n), repeat = r): #product(size of list, length of returned product)
		kmer = ""
		for i in indices: #uses the indicecs to build the kmer to add to answer
			kmer += nucleotides[i]
		answer.append(kmer)
		'''
		if len((indices)) == r: #makes sure the size of the unique value matches r, use set with indices to exclude repeats of same char
			yield tuple(pool[i] for i in indices) #returns the tuple list of kmers
		'''
	for i in answer: #prints each answer out
		print(i)

	return answer #returns the array in case

'''
sample = "T A G C"
k = 2
#required if going the yield route
#test = organizedstring(sample,k)
#for i in test:
#	print(i)
organizedstring(sample,k)
'''

print("")
sample = "E N O F C V D L"
k = 3
organizedstring(sample,k)