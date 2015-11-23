'''
Input: Integers k and d, followed by a collection of strings Dna.
Output: All (k, d)-motifs in Dna. 
'''

def motifenumeration(Dna, k, d):
	patterns = set()
	for seq in Dna:
		for i in range(len(seq) - k):
			pattern = seq[i:i+k]
			for j in range(len(seq) - k):
				test = seq[j:j+k]
				mismatches = 0
				for k in range(k):
					if mismatches < d:
						if pattern[k] != test[k]:
							mismatches += 1
					else:
						break
	return patterns

k = 3
d = 1
input = ['ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT']

patterns = motifenumeration(input, k, d)
print(patterns)