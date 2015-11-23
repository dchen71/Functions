'''
Input: Integers k and d, followed by a collection of strings Dna.
Output: All (k, d)-motifs in Dna. 
'''

def motifenumeration(Dna, k, d):
	patterns = set()
	for i in range(len(Dna) - k):
		pattern = substr(Dna, i , k)
		#for loop to check rest of the string
			#if pattern is in string with at most d mismatch add pattern to patterns
	return patterns