'''
Minimum Skew Problem: Find a position in a genome minimizing the skew.
     Input: A DNA string Genome.
     Output: All integer(s) i minimizing Skewi (Genome) among all values of i (from 0 to |Genome|).
'''

'''
For loop to cycle through genome
Add each skew as the key and position as its value
Call min() to find the minimum
Return using dictionary whatever the min its
re stringify to answer requirements
'''

def minSkew(genome):
	skewed = {}
	num = 0

	for i in range(len(genome)):
		if genome[i] == 'C':
			num -= 1
		elif genome[i] == 'G':
			num += 1
		skewed.setdefault(num,[]).append(i + 1)

	return(skewed[min(skewed)])


#Assertion to check function
assert (minSkew('TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT')) == [11, 24]